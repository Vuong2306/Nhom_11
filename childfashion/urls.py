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
    path('giohang', views.giohang, name='giohang'),
    path('themdm', views.themdm, name='themdm'),
    path('themsp', views.ThemSP, name='themsp'),
    path('chitietsp/<int:product_id>', views.chitietsp, name='chitietsp'),
]
