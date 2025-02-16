from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.html import format_html,urlencode
from django.urls import reverse
from . import models
from django.db.models.aggregates import Count

# Register your models here.

class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'
    
    def lookups(self, request, model_admin):
        return [('<10','Low')]
    
    def queryset(self, request, queryset):
        if self.value == '<10':
         return queryset.filter(inventory__lt = 10)
     
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title','products_count']
    search_fields = ['title']
    
    @admin.display(ordering='products_count')
    def products_count(self,collection):
        url = reverse("admin:store_product_changelist") + '?' + urlencode({"collection__id":collection.id})
        return format_html("<a href={}>{}</a>",url,collection.products_count)
        # return collection.products_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(products_count =Count('product'))



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ['title']
    }
    autocomplete_fields = ['collection']
    actions = ['clear_inventory']

    list_display = ["title","unit_price","inventory_status","collection_title"]
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']
    list_filter = ['collection','last_update',InventoryFilter]
    search_fields = ['product']

    
    def collection_title(self,product):
        return product.collection.title
    
    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory < 10:
            return 'Low'
        return 'Ok'
    
    @admin.action(description="clear_inventory")
    def clear_inventory(self,request,queryset):
        updated_count = queryset.update(inventory = 0)
        self.message_user(request,f'{updated_count} products were updated successfully')
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','membership']
    list_editable = ['membership']
    list_select_related = ['user']
    ordering = ['user__first_name','user__last_name']
    list_per_page = 10
    search_fields = ['first_name__istartswith','last_name__istartswith']
    
# admin.site.register(models.Collection)

# admin.site.register(models.Product,ProductAdmin)

class OrderItemInline(admin.TabularInline):
    autocomplete_fields = ['product']
    model = models.OrderItem
    extra = 0

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = ['id','placed_at','customer']
    list_per_page = 10

    
   