from apps.blog.models import Category, Writer
from django.conf import settings

def get_categories_in_context(request):
    context = {}
    domain  = request.META['HTTP_HOST']
    author = Writer.objects.get(domain_name=domain) 
    categories = Category.objects.all()
    context['categories'] = categories
    context['DEBUG'] = settings.DEBUG
    context['author'] = author
    return context
