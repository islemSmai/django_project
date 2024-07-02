# Generated by Django 4.2.12 on 2024-05-08 17:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('titre', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='shop-images')),
                ('image', models.ImageField(blank=True, null=True, upload_to='shop-images')),
                ('color', models.CharField(max_length=255, null=True)),
                ('color_secondary', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery', models.ImageField(blank=True, null=True, upload_to='shop-images')),
                ('description', models.TextField(blank=True, null=True)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_us', to='shop.shop')),
            ],
        ),
    ]
