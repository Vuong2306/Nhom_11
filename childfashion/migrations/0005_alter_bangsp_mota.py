# Generated by Django 5.0.4 on 2024-05-20 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childfashion', '0004_alter_bangsp_dongia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bangsp',
            name='MoTa',
            field=models.TextField(max_length=1000),
        ),
    ]