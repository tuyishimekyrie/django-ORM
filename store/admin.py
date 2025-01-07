from django.contrib import admin
from django.utils.html import format_html,urlencode
from django.urls import reverse
from . import models
from django.db.models.aggregates import Count
# Register your models here.

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title','products_count']
    
    @admin.display(ordering='products_count')
    def products_count(self,collection):
        url = reverse("admin:store_product_changelist") + '?' + urlencode({"collection__id":collection.id})
        return format_html("<a href={}>{}</a>",url,collection.products_count)
        # return collection.products_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count =Count('product'))

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title","unit_price","inventory_status","collection_title"]
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']

    
    def collection_title(self,product):
        return product.collection.title
    
    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory < 10:
            return 'Low'
        return 'Ok'
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','membership']
    list_editable = ['membership']
    ordering = ['first_name','last_name']
    list_per_page = 10
    search_fields = ['first_name__istartswith','last_name__istartswith']
    
# admin.site.register(models.Collection)

# admin.site.register(models.Product,ProductAdmin)

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','placed_at','customer']
    list_per_page = 10

    
   