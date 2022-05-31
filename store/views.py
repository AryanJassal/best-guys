from django.shortcuts import render

def hyperspectral_tv(request):
    return render(request, 'store/hyperspectral_tv.html', {
        'title_short': 'Hyperspectral TV',
        'title_long': 'Kolofon 69" Quantum Dot 8K Ultra HD Hyperspectral Smart TV',
        'model_number': 'HSTV-69I-UHD-AU09200A',
        'price': '69,420.69',
        # 'sale_price': '1,770.18'
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
