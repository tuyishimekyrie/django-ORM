from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F
from django.db.models.aggregates import Count,Max,Min
from store.models import Product,Customer,Collection,Order,OrderItem
from tags.models import ContentType,Tag,TaggedItem



def say_hello(request):
    # products = Product.objects.all()
    # shoes = Product.objects.earliest("title")
    # customers = Customer.objects.filter(Q(email__endswith=".com") & Q(first_name__icontains="ky") & Q(membership__in="G"))
    # customers = Customer.objects.values_list("first_name")
    # collection = Collection.objects.filter(featured_product__isnull=True)
    # order = Order.objects.filter(customer__id=1)
    # order_item = OrderItem.objects.filter(order_id=F("product_id"))
    # ordered_product_id = OrderItem.objects.values('product_id').distinct()
    # ordered_product = Product.objects.filter(id__in=ordered_product_id).order_by()
    # products = Product.objects.select_related("collection").all()
    # order = Order.objects.select_related("customer").prefetch_related("orderitem_set__product").order_by("-placed_at")[:5]
    # result = Product.objects.aggregate(id=Count("id"))
    # query_set = Product.objects.annotate(Count = Count("id"))
    # query_set = Order.objects.annotate(orders_count= Count("customer_id")).distinct()
    # content_type = ContentType.objects.get_for_model(Product)
    # query_set = TaggedItem.object.select_related("tag").filter(content_type=content_type,object=1)
    # print(query_set)
    # print(result)
    # print(collection)
    # print(products)
    # print(order)
    # print(order_item)
    # print(ordered_product)
    # print(ordered_product_id)
    

    
    
    Collection.objects.filter(pk=1).update(title="Games",featured_product=None)

   
        
    return render(request, 'hello.html', {'name': 'Mosh'})
