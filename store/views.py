from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND,HTTP_200_OK,HTTP_201_CREATED,HTTP_405_METHOD_NOT_ALLOWED
from .models import Product
from .serializer import ProductSerializer
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

@api_view()
def collection_detail(request,pk):
    return Response("Ok")