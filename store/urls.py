from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

routers = DefaultRouter()

routers.register("products",views.ProductListViewSet)
routers.register("collections",views.CollectionListViewSet)

urlpatterns = routers.urls
# urlpatterns = [
#     path('products/',views.ProductList.as_view()),
#     path('product/<int:pk>',views.ProductDetail.as_view()),
#     path('collections',views.CollectionList.as_view()),
#     path('collections/<int:pk>',views.CollectionDetail.as_view(),name="collection_detail")
# ]