from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F
from store.models import Product,Customer,Collection,Order,OrderItem



def say_hello(request):
    products = Product.objects.all()[2:10]
    # shoes = Product.objects.earliest("title")
    # customers = Customer.objects.filter(Q(email__endswith=".com") & Q(first_name__icontains="ky") & Q(membership__in="G"))
    customers = Customer.objects.values_list("first_name")
    collection = Collection.objects.filter(featured_product__isnull=True)
    order = Order.objects.filter(customer__id=1)
    order_item = OrderItem.objects.filter(order_id=F("product_id"))
    ordered_product_id = OrderItem.objects.values('product_id').distinct()
    ordered_product = Product.objects.filter(id__in=ordered_product_id).order_by()
    # print(collection)
    # print(products)
    # print(order)
    # print(order_item)
    print(ordered_product)
    print(ordered_product_id)

   
        
    return render(request, 'hello.html', {'name': 'Mosh',"products":ordered_product})
