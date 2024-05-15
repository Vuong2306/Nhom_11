from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Loai,BangSP
from .forms import TheLoai1Form,TheLoai2Form,ThemLoaiForm

#Create your views here.
def index(request):
   return render(request, 'pages/home.html')

def login(request):
    # Xử lý logic đăng nhập ở đây
    return render(request, 'pages/login.html')

def register(request):
    # Xử lý logic đăng ký ở đây
    return render(request, 'pages/register.html')
# Create your views here.
def menu_top(request):
    # Xử lý logic cho menu_top ở đây
    return render(request, 'pages/menu_top.html')


def DSSP1(request):
    data = {
        "BangSP": BangSP.objects.all(),
    }
    return render(request, 'pages/DSSP1.html', data)


def DSSP2(request):
    data = {
        "BangSP": BangSP.objects.all(),
    }
    return render(request, 'pages/DSSP2.html', data)

def DMLoai(request):
    data = {
        "DMLoai": Loai.objects.all(),
    }
    return render(request, 'pages/DMLoai.html', data)
def TimKiem(request):
    if (request.method == 'POST'):
        searched = request.POST["searched"]
        keys = BangSP.objects.filter(TenSP__contains = searched)
        return render (request, 'pages/TimKiem.html', {"searched": searched, "keys": keys})
def giohang(request):
    # Lấy thông tin giỏ hàng từ cơ sở dữ liệu
    cart_items = BangSP.objects.all()  # Lấy tất cả các sản phẩm từ cơ sở dữ liệu

    # Trả về template "GioHang.html" kèm theo thông tin giỏ hàng
    return render(request, 'pages/GioHang.html', {'cart_items': cart_items})

def themdm(request):
    form = ThemLoaiForm()
    if (request.method == "POST"):
        form = ThemLoaiForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/chilfashion/dmloai')
    return render(request, 'pages/ThemDM.html', {'form': form})

def chitietsp(request, product_id):
    product = get_object_or_404(BangSP, pk=product_id)
    return render(request, 'pages/ChiTietSP.html', {'product': product})

def ThemSP(request):
    form = TheLoai2Form()
    if request.method == "POST":
        form = TheLoai2Form(request.POST)
        if form.is_valid():
            form.save();
            return HttpResponseRedirect('/childfashion/DSSP1')
    return render(request, 'pages/ThemSP.html', {'form': form, 'DMLoai': Loai.objects.all()})

def Men(request):
    product_ids = [1, 4, 5, 6]
    products = BangSP.objects.filter(id__in=product_ids)
    return render(request, 'pages/Men.html', {'BangSP': products})

def Women(request):
    product_ids = [2, 3]
    products = BangSP.objects.filter(id__in=product_ids)
    return render(request, 'pages/Women.html', {'BangSP': products})

def Baby(request):
    product_ids = [1, 2, 5]
    products = BangSP.objects.filter(id__in=product_ids)
    return render(request, 'pages/Baby.html', {'BangSP': products})