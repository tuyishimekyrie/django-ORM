from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from . import views

routers = DefaultRouter()

routers.register("products",views.ProductListViewSet,basename="products")
routers.register("collections",views.CollectionListViewSet)
routers.register("carts",views.CartViewSet)

products_routers = NestedDefaultRouter(routers,'products',lookup='product')
products_routers.register('reviews',views.ReviewViewSet,basename='product-reviews')

cart_routers = NestedDefaultRouter(routers,'carts',lookup='cart')
cart_routers.register('items',views.CartItemViewSet,basename='cart-items')



urlpatterns = routers.urls + products_routers.urls + cart_routers.urls
# urlpatterns = [
#     path('products/',views.ProductList.as_view()),
#     path('product/<int:pk>',views.ProductDetail.as_view()),
#     path('collections',views.CollectionList.as_view()),
#     path('collections/<int:pk>',views.CollectionDetail.as_view(),name="collection_detail")
# ]