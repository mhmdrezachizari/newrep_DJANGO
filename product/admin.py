from django.contrib import admin
from .models import PRODUCTS,Category , TOPVBANNER
@admin.register(PRODUCTS)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'image',)
    search_fields = ('name',)
    list_filter = ('price', 'image')

admin.site.register(Category)
admin.site.register(TOPVBANNER)