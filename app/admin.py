from django.contrib import admin
from app.models import Category, Product, Tag

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'get_tags', 'is_active', ]
    list_filter = ['is_active']
    search_fields = ['name']

    def get_tags(self, obj):
        return ", \n".join([t.name for t in obj.tags.all()])

    get_tags.short_description = 'tags'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Product, ProductAdmin)
