from apps.blog.models import Category
from django.conf import settings

def get_categories_in_context(request):
    context = {}
    categories = Category.objects.all()
    context['categories'] = categories
    context['DEBUG'] = settings.DEBUG
    return context
