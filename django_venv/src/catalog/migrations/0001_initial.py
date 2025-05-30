# Generated by Django 5.2.1 on 2025-05-14 11:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(default='default_slug', unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(default='default_slug', unique=True, verbose_name='URL')),
                ('sku', models.CharField(default='000000', max_length=50, unique=True, verbose_name='Артикул')),
                ('short_description', models.TextField(default='', verbose_name='Краткое описание')),
                ('full_description', models.TextField(default='', verbose_name='Полное описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Старая цена')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Основное изображение')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Доп. изображение 1')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Доп. изображение 2')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Доп. изображение 3')),
                ('material', models.CharField(default='', max_length=100, verbose_name='Материал')),
                ('dimensions', models.CharField(default='0x0x0', max_length=100, verbose_name='Размеры (Ш x Г x В)')),
                ('weight', models.DecimalField(decimal_places=2, default='0.00', max_digits=6, verbose_name='Вес (кг)')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100, verbose_name='Автор')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], verbose_name='Рейтинг')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='catalog.product')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['-created_at'],
            },
        ),
    ]
