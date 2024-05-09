from django.db import models

class Loai(models.Model):
    TenLoai = models.CharField(max_length=100)
  
class BangSP(models.Model):
    TenSP = models.CharField(max_length=100)
    DonGia = models.CharField(max_length=100)
    HinhAnh = models.CharField(max_length=100)
    MoTa = models.TextField(max_length=100)
    PhuKien = models.CharField(max_length=100)
    KichThuoc = models.CharField(max_length=100)
    MauSac = models.CharField(max_length=100)
    ML = models.ForeignKey(Loai, on_delete = models.CASCADE, related_name='BangSP')
  
