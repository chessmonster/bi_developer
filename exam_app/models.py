from django.urls import reverse
from django.db import models


class test_table(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('exam_app:detail', args=[str(self.id)])

class Package(models.Model):
	id = models.IntegerField(primary_key = True)
	address = models.CharField(max_length=250)
	major_region = models.CharField(max_length=250)
	package_number = models.CharField(max_length=250)
	shipped_at = models.DateTimeField(max_length=250)
	delivered_at = models.DateTimeField(max_length=250)
	leadtime = models.FloatField(max_length=250, null = True)

class Region(models.Model):
	id = models.IntegerField(primary_key = True)
	region = models.CharField(max_length=250)
	major_region = models.CharField(max_length=250)

class ImsSalesOrderItemStatus(models.Model):
	id_sales_order_item_status = models.IntegerField(primary_key = True)
	fk_oms_function = models.IntegerField()
	status = models.CharField(max_length=250)
	desc = models.CharField(max_length=250)
	deprecated = models.CharField(max_length=250)
	updated_at = models.DateTimeField(max_length=250)

class ImsSalesOrderItem(models.Model):
	id_sales_order_item = models.IntegerField(primary_key = True)
	bob_id_sales_order_item = models.IntegerField()
	fk_sales_order = models.IntegerField()
	fk_sales_order_item_status = models.ForeignKey('ImsSalesOrderItemStatus', on_delete=models.PROTECT)
	fk_delivery_type = models.IntegerField()
	unit_price = models.FloatField(max_length = 250)	
	tax_amount = models.IntegerField()
	paid_price = models.FloatField(max_length = 250)	
	name = models.CharField(max_length=250)
	sku = models.CharField(max_length=250)
	created_at = models.DateTimeField(max_length=250)
	updated_at = models.DateTimeField(max_length=250)	
	last_status_change = models.DateTimeField(max_length=250)
	original_unit_price = models.FloatField(max_length = 250)
	shipping_type = models.CharField(max_length=250)
	real_delivery_date = models.DateTimeField(max_length=100, null=True)
	bob_id_supplier	= models.IntegerField()
	is_marketplace = models.IntegerField()

class ImsSalesOrderItemStatusHistory(models.Model):
	id_sales_order_item_status_history = models.IntegerField(primary_key = True)
	fk_sales_order_item	= models.ForeignKey('ImsSalesOrderItem', on_delete=models.PROTECT)
	fk_sales_order_item_status = models.ForeignKey('ImsSalesOrderItemStatus', on_delete=models.PROTECT)
	created_at = models.DateTimeField(max_length=100, null=True)



