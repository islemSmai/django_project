from django.db import models
from django.contrib.auth.models import User
class Shop(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255,null=True)
    description = models.TextField(blank=True,null=True)
    titre = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='shop-images',blank=True,null=True)
    image = models.ImageField(upload_to='shop-images',blank=True,null=True)
    color = models.CharField(max_length=255,null=True)
    color_secondary = models.CharField(max_length=255,null=True)
    profit = models.FloatField(default=0)
    created_by = models.OneToOneField(User,related_name='items',on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
class AboutUs(models.Model):
    shop = models.ForeignKey(Shop, related_name='about_us', on_delete=models.CASCADE)
    gallery = models.ImageField(upload_to='shop-images',blank=True,null=True)
    description = models.TextField(blank=True,null=True)

