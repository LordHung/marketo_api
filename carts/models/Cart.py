from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete, pre_save, post_save

User = settings.AUTH_USER_MODEL


class Cart(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	items = models.ManyToManyField('Product', through='CartItem')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	subtotal = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
	total = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
	active = models.BooleanField(default=True)

	def __str__(self):
		return str(self.id)	

	def update_subtotal(self):
		print('Update Subtotal....')		
		subtotal = 0
		items = self.cartitem_set.all()	
		for item in items:
			subtotal += item.line_item_total
		self.subtotal = '%.2f' %(subtotal)
		self.save()
		
	def is_complete(self):
		self.active = False
		self.save()

	class Meta:
		db_table = 'cart'
