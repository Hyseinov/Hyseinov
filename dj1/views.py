from django.http import HttpResponse, request
from django.shortcuts import render, redirect

from dj1.forms import CategoryForms
from dj1.models import Product, Review, Category


def get_all_products(request):
    products = Product.objects.all()
    return render(request, "product.html", context={"products": products})


def get_one_product(request, id):
    product = Product.objects.filter(id=id).first()
    review = Review.objects.filter(product_id=id)
    count_rew = review.count()
    return render(request, "detail.html", context={"product": product,"review":review, "count_rew":count_rew})

def categori_form(request):
    form = CategoryForms(request.POST)
    if form.is_valid():
        Category.objects.create(name=request.POST['name'])
        return redirect("products")
    return render(request, "form.html", context={"form": form})
