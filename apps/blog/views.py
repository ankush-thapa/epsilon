from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import json

# internal imports
from apps.blog.models import ContactMe
from apps.blog.models import Blog
from apps.blog import constants

def homepage(request, template='homepage.html'):
    blogs = Blog.objects.filter(status=constants.BLOG_STATUSES['published']).order_by('-created_on')
    context = { 
            'blogs':blogs,
        }   
    return render_to_response(template, context, context_instance=RequestContext(request))

def blog_page(request, slug, template='blog.html'):
    blogs = Blog.objects.filter(slug=slug)
    views = blogs[0].views
    blogs.update(views=views+1)
    try:
        next_blog = Blog.objects.get(id=blogs[0].id-1)
    except Blog.DoesNotExist:
        next_blog = None
    context = { 
            'blog':blogs[0],
            'next_blog':next_blog,
        }   
    return render_to_response(template, context, context_instance=RequestContext(request))

@csrf_exempt
def contact_me(request):
    if request.method != "POST":
       return ''
    contact_me = ContactMe()
    contact_me.contact_name = request.POST.get('name')
    contact_me.email = request.POST.get('email')
    contact_me.phone_number = request.POST.get('phone')
    contact_me.message = request.POST.get('message')
    contact_me.save()
    # send email here
    #message = ""
    #send_mail('SUBJECT', message, settings.EMAIL_HOST_USER,
    #    ['namratajain61@gmail.com', 'ankushiitb@gmail.com'], fail_silently=False)
    response = {'status':1}
    return HttpResponse(json.dumps(response), content_type="application/json")
    
def category_page(request, category, category_id, template='homepage.html'):
    blogs = Blog.objects.filter(status=constants.PUBLISHED_STATUS, category=category_id).order_by('-created_on')
    context = { 
            'blogs':blogs,
            'category':blogs.values_list('category__name', flat=True)
        }   
    return render_to_response(template, context, context_instance=RequestContext(request))
