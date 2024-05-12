# Generated by Django 5.0.4 on 2024-05-08 15:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenLoai', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BangSP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenSP', models.CharField(max_length=100)),
                ('DonGia', models.CharField(max_length=100)),
                ('HinhAnh', models.CharField(max_length=100)),
                ('MoTa', models.TextField(max_length=100)),
                ('PhuKien', models.CharField(max_length=100)),
                ('KichThuoc', models.CharField(max_length=100)),
                ('MauSac', models.CharField(max_length=100)),
                ('ML', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BangSP', to='childfashion.loai')),
            ],
        ),
    ]