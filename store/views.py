from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND,HTTP_200_OK,HTTP_201_CREATED,HTTP_405_METHOD_NOT_ALLOWED
from .models import Product,Collection
from .serializer import ProductSerializer,CollectionSerializer
from django.db.models.aggregates import Count
# Create your views here.

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        queryset  = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(queryset,many=True,context = {"request":request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data =request.data)
        serializer.is_valid(raise_exception=True)
        # print(serializer.validated_data)  
        serializer.save() 
        return Response(serializer.data,status = HTTP_201_CREATED)



@api_view(['GET','PUT','DELETE'])    
def product_detail(request,id):
    product = get_object_or_404(Product,pk=id)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status = HTTP_200_OK)
    else:
        if product.orderitems.count() > 0:
            return Response({'error':'This item cannot be deleted'})
        product.delete()
        return Response(status=HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET','POST'])
def collections(request):
    if request.method == 'GET':
     queryset = Collection.objects.annotate(products_count = Count('products')).all()
     collection = CollectionSerializer(queryset,many=True)
     return Response(collection.data,status=HTTP_200_OK)
    else:
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=HTTP_201_CREATED)

@api_view(['Get','PUT','DELETE'])
def collection_detail(request,pk):
    collection = get_object_or_404(Collection.objects.annotate(products_count = Count('products')),pk=pk)
    if request.method == 'GET':
        serializer = CollectionSerializer(collection)        
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer =CollectionSerializer(collection,data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data,status=HTTP_200_OK)
    else:
        if collection.products.count()  > 0:
            return Response({"error":"This collection cannot be deleted because it is associated with some products"})
        collection.delete()
        return Response({"success":"Collection deleted successully"},status=HTTP_200_OK)