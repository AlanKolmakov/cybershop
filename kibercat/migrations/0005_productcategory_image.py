# Generated by Django 4.0.4 on 2022-07-08 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kibercat', '0004_product_image_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='image',
            field=models.ImageField(blank=True, upload_to='products_images/Catalog', verbose_name='Фото'),
        ),
    ]
