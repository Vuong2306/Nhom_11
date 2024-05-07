from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('menu_top/', views.menu_top, name='menu_top'),  # Đường dẫn cho trang menu_top
    path('register/', views.register, name='register'),
    # path('gioi-thieu/', views.about, name='about'),
    # path('tin-tuc/', views.news, name='news'),
    # path('san-pham/', views.products, name='products'),
    # path('lien-he/', views.contact, name='contact'),
    # path('khuyen-mai/', views.promotions, name='promotions'),
]
