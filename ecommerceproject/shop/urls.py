
from django.urls import path
from . import views

urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),  # Add this line for the root path
    path('<slug:c_slug>/', views.allProdCat, name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),
]
