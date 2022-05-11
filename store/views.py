from django.shortcuts import render

def product_page(request, product_id):
    if product_id == 0:
        title = 'Hyperspectral TV'
    else:
        title = 'Uh-oh'

    return render(request, 'store/product_information.html', {
        'title': title
    })
