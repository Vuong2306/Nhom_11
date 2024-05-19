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
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = BangSP.objects.filter(TenSP__icontains = searched)
        return render(request, 'pages/TimKiem.html', {"searched": searched, "keys":keys})
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
    if request.method == "POST":
        form = TheLoai2Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/childfashion/dssp1')
    else:
        form = TheLoai2Form()
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
def addToCart(request, id):
    product = BangSP.objects.get(id=id)
    cart = []
    if 'cart' in request.session:
        cart = request.session['cart']
    
    updateCart = []
    inCart = False
    for cartProduct in cart:
        currentId = cartProduct.get('id')
        if currentId == product.id:
            inCart = True
            cartProduct['quantity'] = int(cartProduct['quantity']) + 1
        updateCart.append(cartProduct)
        
    if inCart == False:
        updateCart.append({
            'id': product.id,
            'name': product.TenSP,
            # 'hinhanh': product.HinhAnh,
            'price': product.DonGia,
            'quantity': 1,
        }) 
    request.session['cart'] = updateCart

    return HttpResponseRedirect('/childfashion/dssp2')


def viewCart(request):
    cart = None
    if 'cart' in request.session:
        cart = request.session['cart']
    print(cart)
    return render(request, 'pages/GioHang.html', {'cart':cart})
def clearCart(request):
    del request.session['cart']
    return HttpResponseRedirect('/childfashion/giohang')
def deleteToCart(request,id):
    cart = []
    if 'cart' in request.session:
        cart = request.session['cart']
    
    updateCart = []
    for cartProduct in cart:
        currentId = cartProduct.get('id')
        if currentId != id:
            updateCart.append(cartProduct)

    request.session['cart'] = updateCart
        
    return HttpResponseRedirect('/childfashion/giohang')

def updateQuantity(request, id):
    quantity = int(request.POST['quantity'])
    product = BangSP.objects.get(id=id)
    cart = []
    if 'cart' in request.session:
        cart = request.session['cart']
    
    updateCart = []
    inCart = False
    for cartProduct in cart:

        currentId = cartProduct.get('id')
        print(currentId)
        if currentId == product.id:
            inCart = True
            cartProduct['quantity'] = quantity
        updateCart.append(cartProduct)
        
    if inCart == False:
        updateCart.append({
            'id': product.id,
            'name': product.TenSP,
            # 'hinhanh': product.HinhAnh,
            'price': product.DonGia,
            'quantity': quantity,
        }) 
    request.session['cart'] = updateCart
    return HttpResponseRedirect('/childfashion/giohang')

