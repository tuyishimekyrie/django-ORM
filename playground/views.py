from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F
from store.models import Product,Customer,Collection,Order,OrderItem



def say_hello(request):
    products = Product.objects.filter(inventory__lt="10")
    customers = Customer.objects.filter(Q(email__endswith=".com") & Q(first_name__icontains="ky") & Q(membership__in="G"))
    collection = Collection.objects.filter(featured_product__isnull=True)
    order = Order.objects.filter(customer__id=1)
    order_item = OrderItem.objects.filter(order_id=F("product_id"))
    # print(collection)
    # print(products)
    # print(order)
    print(order_item)

   
        
    return render(request, 'hello.html', {'name': 'Mosh',"customers":customers})
