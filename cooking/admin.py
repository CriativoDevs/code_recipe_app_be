from django.contrib import admin
from .models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)