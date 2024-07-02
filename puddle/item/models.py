from django.db import models
from shop.models import Shop
class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='item-images',blank=True,null=True)
    shop = models.ForeignKey(Shop,related_name='shops',on_delete=models.CASCADE)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name
class Item(models.Model):
    category = models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item-images',blank=True,null=True)
    quantity = models.IntegerField()
    is_sold = models.BooleanField(default=False)
    #created_by = models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
class Image(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    gallery = models.ImageField(upload_to='item-images',blank=True,null=True)
