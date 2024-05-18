from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('menu_top/', views.menu_top, name='menu_top'),  # Đường dẫn cho trang menu_top
    path('register/', views.register, name='register'),
    path('search', views.TimKiem, name='search'),
    path('dssp1', views.DSSP1, name='dssp1'),
    path('dssp2', views.DSSP2, name='dssp2'),
    path('dmloai', views.DMLoai, name='dmloai'),
    path('giohang', views.viewCart, name='giohang'),
    path('themdm', views.themdm, name='themdm'),
    path('themsp', views.ThemSP, name='themsp'),
    path('chitietsp/<int:product_id>', views.chitietsp, name='chitietsp'),
    path('men', views.Men, name='men'),
    path('women', views.Women, name='women'),
    path('baby', views.Baby, name='baby'),
    path('addToCart/<int:id>', views.addToCart, name='addtocart'),
    path('deleteToCart/<int:id>', views.deleteToCart, name='deletetocart'),
    path('updateQuantity/<int:id>', views.updateQuantity, name='updatequantity'),
    path('clearCart', views.clearCart, name='clearcart'),
]
