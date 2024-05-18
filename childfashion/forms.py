from django import forms
from .models import Loai, BangSP

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