from django.db import models
import os

def upload_image_to(instance, filename):
    return os.path.join('static/images', filename)
class Loai(models.Model):
    TenLoai = models.CharField(max_length=100)
  
class BangSP(models.Model):
    TenSP = models.CharField(max_length=100)
    DonGia = models.CharField(max_length=100)
    HinhAnh = models.ImageField(upload_to=upload_image_to) # Sử dụng hàm upload_image_to để lưu tệp
    MoTa = models.TextField(max_length=100)
    PhuKien = models.CharField(max_length=100)
    KichThuoc = models.CharField(max_length=100)
    MauSac = models.CharField(max_length=100)
    SoLuong = models.IntegerField(null=True, blank=True)
    ML = models.ForeignKey(Loai, on_delete=models.CASCADE, related_name='BangSP')

    def save(self, *args, **kwargs):
        # Lưu tệp hình ảnh vào vị trí cụ thể
        super().save(*args, **kwargs)
        # Chỉ lưu tên tệp vào cơ sở dữ liệu
        if self.HinhAnh:
            self.HinhAnh.name = os.path.basename(self.HinhAnh.name)
            super().save(*args, **kwargs)
