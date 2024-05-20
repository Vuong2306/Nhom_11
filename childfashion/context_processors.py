from .models import Loai,BangSP
from django.shortcuts import render,get_object_or_404

def categories(request):
    categories = Loai.objects.all()
    return {
        'categories':categories
    }

def category_products(request, category_id):
    category = get_object_or_404(Loai, pk=category_id)
    products = BangSP.objects.filter(ML=category)
    return render(request, 'pages/DSSP2.html', {'BangSP': products, 'category': category})