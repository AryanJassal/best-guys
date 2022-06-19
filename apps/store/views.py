from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import *

# def products(request, filter):
#     return HttpResponse('testing worked')

def product_details(request, slug):
    product = Product.objects.get(slug=slug)
    discount_percent = round(((product.price - product.sale_price) / product.price) * 100, 2)

    paginator = Paginator(product.reviews.all(), 10)
    page_number = request.GET.get('page')
    paginated_reviews = paginator.get_page(page_number)

    return render(request, 'store/product_layout.html', {
        'product': product,
        'discount_percent': discount_percent if discount_percent > 99 else round(discount_percent),
        'paginated_reviews': paginated_reviews
    })

def new_review(request, slug):
    if request.method == 'POST':
        # request_user = request.user
        new_review = Review(
            user=request.user if request.user.is_authenticated else None,
            title=request.POST.get('title'),
            body=request.POST.get('review'),
            recommended=True if request.POST.get('recommended') else False,
            star_rating=5 if request.POST.get('star-rating') == '' else int(request.POST.get('star-rating'))
        )
        new_review.save()

        product = Product.objects.get(slug=slug)
        product.reviews.add(new_review)
        product.save()
        
        return redirect('store:product_details', slug=slug)

def delete_review(request, slug, pk):
    product = Product.objects.get(slug=slug)
    review = product.reviews.get(pk=pk)
    review.delete()
    return redirect('store:product_details', slug=product.slug)
