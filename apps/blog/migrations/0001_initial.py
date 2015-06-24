# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300, db_column=b'title')),
                ('slug', models.SlugField(max_length=300, null=True, db_column=b'slug', blank=True)),
                ('short_description', models.CharField(max_length=500, db_column=b'shortdescription')),
                ('content', tinymce.models.HTMLField(null=True, db_column=b'content', blank=True)),
                ('views', models.IntegerField(default=0, db_column=b'views')),
                ('shares', models.IntegerField(default=0, db_column=b'shares')),
                ('status', models.SmallIntegerField(db_column=b'status', choices=[(1, b'draft'), (2, b'published'), (3, b'deleted')])),
                ('tags', models.CharField(max_length=500, null=True, db_column=b'tags', blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_column=b'createdon')),
                ('moderated_on', models.DateTimeField(null=True, db_column=b'moderatedon', blank=True)),
                ('last_modified_on', models.DateTimeField(null=True, db_column=b'lastmodifiedon', blank=True)),
                ('header_image', models.ImageField(null=True, upload_to=b'blog/static/images/', db_column=b'header_image', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, db_column=b'name')),
            ],
        ),
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PublicImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'blog/static/images/', db_column=b'header_image', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(to='blog.Category', db_column=b'category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='written_by',
            field=models.ForeignKey(blank=True, to='blog.Writer', null=True),
        ),
    ]
