from django.template.defaultfilters import slugify
from django.contrib.sitemaps import ping_google
from django.contrib.sitemaps import Sitemap
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db import models
from apps.blog import constants
from apps.blog import choices

class Blog(models.Model):
    title = models.CharField(max_length=300, db_column='title')
    slug = models.SlugField(max_length=300, db_column='slug', null=True, blank=True)
    short_description = models.CharField(max_length=500, db_column='shortdescription')
    content = HTMLField(db_column='content', blank = True, null = True)
    views = models.IntegerField(default=0, db_column='views')
    shares = models.IntegerField(default=0, db_column='shares')
    written_by = models.ForeignKey('Writer', null=True, blank=True)
    category = models.ManyToManyField('Category', db_column='category')

    status = models.SmallIntegerField(choices=choices.BLOG_STATUSES, db_column='status')
    tags = models.CharField(max_length=500, null=True, blank=True, db_column='tags')
    created_on = models.DateTimeField(auto_now_add=True, db_column='createdon')
    moderated_on = models.DateTimeField(null=True, blank=True, db_column='moderatedon')
    last_modified_on = models.DateTimeField(null=True, blank=True, db_column='lastmodifiedon')
    header_image = models.ImageField(upload_to = 'static/images/', null=True, blank=True, db_column='header_image')

    def __unicode__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def get_url(self):
        return '/blog/' + slugify(self.title) + '/'

    def get_header_image_url(self):
	name = self.header_image.name.split('/')[-1]
        return '%s' % str(name)

class Writer(User):
    cover_image = models.ImageField(upload_to = 'static/images/', null=True, blank=True, db_column='cover_image')
    domain_name = models.CharField(max_length=100, db_column='domain_name')

    # blog details
    blog_name = models.CharField(max_length=100, db_column='blog_name')
    blog_tagline = models.CharField(max_length=100, db_column='blog_tagline')
    blog_meta_title = models.CharField(max_length=150, db_column='blog_meta_title')
    blog_meta_description = models.CharField(max_length=300, db_column='blog_meta_description')
    blog_meta_keywords = models.CharField(max_length=500, db_column='blog_meta_keywords')
    facebook_link = models.CharField(max_length=100, db_column='facebook_link')
    twitter_link = models.CharField(max_length=100, db_column='twitter_link')
    gplus_link = models.CharField(max_length=100, db_column='gplus_link')

    def __unicode__(self):
        return str(self.first_name)
    
class Category(models.Model):
    name = models.CharField(max_length=100, db_column='name')

    def __unicode__(self):
        return str(self.name)

    def get_url(self):
	return '/'+slugify(self.name)+'/'+str(self.id)

class ContactMe(models.Model):
    contact_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    message = models.TextField()
    def __unicode__(self):
        return str(self.contact_name)

class PublicImage(models.Model):
    image = models.ImageField(upload_to = 'static/images/', null=True, blank=True, db_column='header_image') 

    def __unicode__(self):
	name = self.image.name.split('/')[-1]
        return '%s' % str(name)

class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 1.0 

    def items(self):
        return Blog.objects.filter(status=constants.BLOG_STATUSES['published']).order_by('-created_on')

    def lastmod(self, obj):
        return obj.last_modified_on
    
    def location(self, obj):
        return '/' + str(obj.slug) + '/' 
