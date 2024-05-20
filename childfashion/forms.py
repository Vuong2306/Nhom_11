from django import forms
from .models import Loai, BangSP
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.forms import ModelForm


class ThemLoaiForm(forms.Form):
    TenLoai = forms.CharField(label = 'Tên thể loại', max_length=100)

    def clean_TenLoai(self):
        TenLoai = self.cleaned_data['TenLoai']
        try:
            Loai.objects.get(TenLoai = TenLoai)
        except Loai.DoesNotExist:
            return TenLoai
        raise forms.ValidationError("Tên loại đã tồn tại")
    def save(self):
        Loai.objects.create(TenLoai = self.cleaned_data['TenLoai'])

class TheLoai1Form(forms.ModelForm):

    class Meta:
        model = Loai
        fields = ["TenLoai"]

class TheLoai2Form(forms.ModelForm):
    class Meta:
        model = BangSP
        fields = ['TenSP', 'DonGia', 'ML', 'HinhAnh', 'MoTa']

class BangSPForm(forms.ModelForm):
    class Meta:
        model = BangSP
        fields = ['TenSP', 'DonGia', 'HinhAnh', 'MoTa', 'KichThuoc', 'MauSac', 'ML']        

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài khoản', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.match(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản chỉ được chứa kí tự chữ, số và dấu gạch dưới")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")

    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])