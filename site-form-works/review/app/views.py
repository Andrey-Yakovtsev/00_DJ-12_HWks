from django import forms
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    reviews = Review.objects.select_related('product').all()
    review_count = request.session.get('has_review')
    request.session['has_review'] = review_count
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(text=form.cleaned_data['text'], product_id=pk)
            review_count.append(pk)
            return redirect('product_detail', product.id)
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'product': product,
        'reviews': reviews.filter(product_id=pk),
        'has_review': request.session['has_review']
    }

    return render(request, template, context)
