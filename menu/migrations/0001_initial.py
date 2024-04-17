# Generated by Django 4.2.7 on 2024-04-17 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Назва')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категорію',
                'verbose_name_plural': 'Категорії',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Dishs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Назва')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('image', models.ImageField(blank=True, null=True, upload_to='menu_images', verbose_name='Зображення')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Ціна')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Знижка у %')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.categories', verbose_name='Категорія')),
            ],
            options={
                'verbose_name': 'Страву',
                'verbose_name_plural': 'Страви',
                'db_table': 'dish',
            },
        ),
    ]
