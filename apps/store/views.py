from django.shortcuts import render
from django.urls import reverse
from django.templatetags.static import static
from django.http import HttpResponse

from .models import *

def hyperspectral_tv(request):
    product = Product.objects.get(slug='hyperspectral-tv')
    price = product.price
    discount_percent = round(((product.price - product.sale_price) / product.price) * 100, 2)

    return render(request, 'store/page_layout.html', {
        'product': product,
        'discount_percent': discount_percent if discount_percent > 99 else round(discount_percent),
        'breadcrumbs': {
            'Products': reverse('store:products', kwargs={'filter': 'all'}),
            'Televisions': reverse('store:products', kwargs={'filter': 'televisions'}),
            'Kolofon Hyperspectral TV': '',
        }
    })

def glass_s(request):
    price = 499
    sale_price = 199
    return render(request, 'store/page_layout.html', {
        'title_short': 'Kolofon Glass-S',
        'title_long': 'Kolofon Proprietary Hyperspectral Glass-S',
        'model_number': 'KFHSGL691-2020V-STDSZ-AU04561D',
        'product_image': static('images/glass-s.png'),
        'price': price,
        'sale_price': sale_price,
        'discount_percent': round(((price - sale_price) / price) * 100),
        'brief_description': 'Kolofon 69\" Quantum Dot 16K Ultra HD Hyperspectral Smart TV has a high-resolution 16K UHD display so you never miss a single detail. Powered by the Quantum Dot pixel technology, the refresh rates are blazingly fast! The quantum dot technology also enables the Hyperspectral TV to display extremely vivid colours and high contrast for maximum immersion, along with Quantum HDR 16X Plus support! This makes the Hyperspectral TV the perfect solution for the ultimate entertainment experience. The massive 69\" screen size ensures that all your family can watch the latest and greatest shows together with a cinema-like experience! Powered by the proprietary KF Zenith T27 processor and packed with 8GB of RAM, the Kolofon Hyperspectral TV can handle whatever you throw at it with ease. Its massive 1TB SSD storage makes it easy to store all your digital content and applications. The Hyperspectral TV also offers built-in Wi-Fi 6 and Bluetooth 6.0 connectivity! Thanks to Kolofon\'s latest breakthrough in hyperspectral image rendering, the Hyperspectral TV is able to display two individual display inputs at the same time so there will be no more fights regarding whose time it is to watch the television! Simply wear a pair of Glass-S™ (sold separately) and a pair of headphones (not included, sold separately)! Thats it! You can now start using the second hyperspectral layer to play whatever you want to watch without disturbing the first hyperspectral layer!',
        'technical_specifications': {
            'Screen Technology: ': 'Fourth Generation Quantum Dot Hyperspectral Panel',
            'Screen Size: ': '69\"',
            'Screen Resoluion: ': '15360 x 8640',
            'Colour Technology': '400% sRGB, 64-bit colour depth',
            'Hyperspectral: ': 'Yes',
            'Simultaneous Hyperspectral Chanels: ': '2',
            'Storage Type: ': 'NVMe Solid State Drive',
            'Storage Read Speed (Storage Write Speed): ': '6250MB/s (4800MB/s)',
            'Storage Capacity: ': '1TB',
            'Webcam: ': 'Yes',
            'Webcam Resolution: ': '2560 x 1440 (144Hz)',
            'TV Processor': 'Kolofon KF Zenith T27 Processor',
            'Smart TV: ': 'Yes',
            'Smart TV Platform: ': 'KF HyperOS 1.4',
            '3D Compatible: ': 'Yes',
            'Bluetooth: ': 'Bluetooth 6.1',
            'Wireless Protocol: ': 'WiFi 6',
            'Compatible Video Streaming Apps: ': 'All',
            'Built-in Voice Assistant: ': 'Google Assistant, Amazon Alexa, Hyper AI',
            'HDR Format: ': 'Quantum HDR 16X Plus',
            'Sound: ': 'InfiniImmersion Pro',
            'Refresh Rate': 'Variable',
            'Maximum Refresh Rate: ': '690Hz',
            'Motion Rate: ': '0.1μs',
            'HDMI Inputs: ': '5',
            'DisplayPort Inputs': '2',
            'USB Inputs: ': '6',
            'Energy Star Rating: ': '9.5 stars',
            'Release Year: ': '2022',
            'Series: ': 'Hyperspectral Series (KFHSTV027)',
            'Weight with stand (weight without stand): ': '36kg (29kg)',
            'What\'s In The Box: ': '2x HyperWave Remote, 2x DisplayPort 2.0',
            'Additional Features: ': 'Fire Resistant (Class 0 Fire Rating), Water Resistant (IP69KX Rating)',
            'Manufacturer\'s Warranty *': '3 Years',
        },
        'breadcrumbs': {
            'Products': reverse('store:products', kwargs={'filter': 'all'}),
            'Televisions': reverse('store:products', kwargs={'filter': 'televisions'}),
            'Kolofon Hyperspectral TV': '',
        }
    })

def products(request, filter):
    return HttpResponse('testing worked')
