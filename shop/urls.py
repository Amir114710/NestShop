from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('' , views.ProductsList.as_view() , name='shop_main'),
    path('<slug:slug>' , views.ProductDetail.as_view() , name='datail'),
    path('category/<int:pk>', views.CategoryDetails.as_view() , name='category_detail'),
    path('like/<slug:slug>/<int:pk>' , views.like , name='like'),
    path('likes_list/' , views.LikeListView.as_view() , name='likes_list'),
    path('likes_delete/<slug:slug>' , views.LikeDeleteView.as_view() , name='likes_delete'),
    path('compares_list/' , views.CompareListView.as_view() , name='compares_list'),
    path('compare/<slug:slug>' , views.Compares.as_view() , name='compares'),
    path('compares_delete/<slug:slug>' , views.CompareDeleteView.as_view() , name='compares_delete'),
]
