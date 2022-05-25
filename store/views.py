from django.shortcuts import render

def hyperspectral_tv(request):
    return render(request, 'store/hyperspectral_tv.html', {
        'title': 'Hyperspectral TV',
        # 'breadcrumbs': {
        #     'Products': 'store/products/all',
        #     'Televisions': 'store/products/televisions'
        #     'Hyperspectral TV'
        # }
    })

def glass_s(request):
    return render(request, 'store/glass_s.html')

# def all_products(request):
#     pass

# def products_television(request):
#     pass

# def products_accessories(request):
#     pass

# def products_television_accessories(request):
#     pass
