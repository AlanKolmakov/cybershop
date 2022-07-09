# Generated by Django 4.0.4 on 2022-06-09 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kibercat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaruselSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carusel_img', models.ImageField(upload_to='slider_image')),
                ('carusel_title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('carusel_text', models.CharField(max_length=255, verbose_name='Текст')),
                ('carusel_css', models.CharField(default='-', max_length=255, null=True, verbose_name='CSS класс')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'Каталог товара', 'verbose_name_plural': 'Каталог товаров'},
        ),
        migrations.AlterField(
            model_name='product',
            name='article_name',
            field=models.CharField(db_index=True, max_length=64, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(default=0, verbose_name='Скидка %'),
        ),
        migrations.AlterField(
            model_name='product',
            name='full_description',
            field=models.TextField(blank=True, verbose_name='Характеристики'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Доступность'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=64, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(verbose_name='Остаток'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Доступность'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='products_images/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Доступность'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='На главной'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]