from django.contrib import admin
from django.urls import path
from dj1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.get_all_products, name="products"),
    path('products/<int:id>/', views.get_one_product),
    path('form/', views.categori_form)
]
