from django.shortcuts import render
from django.http import HttpResponse
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