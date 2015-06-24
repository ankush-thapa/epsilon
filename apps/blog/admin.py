from apps.blog.models import Blog, Writer, Category, ContactMe, PublicImage
from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):
    def show_preview_url(obj):
        return '<a target="_blank" href="/blog/%s">%s (click here to preview)</a>' % (obj.slug, obj.slug)
    show_preview_url.allow_tags = True
    list_display = ('title', 'status', 'written_by')
    list_filter = ('status', 'written_by')
    list_editable = ('status', )
    search_fields = ('title', 'content', 'short_description')
    readonly_fields = ('last_modified_on', show_preview_url)
    exclude = ('moderated_on', 'shares')
admin.site.register(Blog, BlogAdmin)

class WriterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Writer, WriterAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)

class ContactMeAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'email', 'phone_number', 'message')
    search_fields = ('contact_name', 'email', 'phone_number', 'message')
    readonly_fields = ('contact_name', 'email', 'phone_number', 'message')
admin.site.register(ContactMe, ContactMeAdmin)

class PublicImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(PublicImage, PublicImageAdmin)
