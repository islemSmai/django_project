from django.db import models
from django.db import models
from item.models import Item
class Payment(models.Model):
	email = models.CharField(max_length=255)
	product = models.ForeignKey(Item,related_name='items', on_delete=models.CASCADE)
	payment_bool = models.BooleanField(default=False)
	stripe_checkout_id = models.CharField(max_length=500)
	purchaseDate = models.DateField(auto_now_add=True)
	amount= models.FloatField()
	class Meta:
		ordering = ('email',)
	def __str__(self):
		return self.email
