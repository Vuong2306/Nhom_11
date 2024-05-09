from django.shortcuts import render
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
    return render(request, 'pages/GioHang.html')

def themdm(request):
    form = ThemLoaiForm()
    if (request.method == "POST"):
        form = ThemLoaiForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/chilfashion/dmloai')
    return render(request, 'pages/ThemDM.html', {'form': form})
