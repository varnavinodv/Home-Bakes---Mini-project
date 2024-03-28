from django.db import models
from customer.models import Customer
from baker.models import Baker
from product.models import Product

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    # customer_id = models.IntegerField()
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    # baker_id = models.IntegerField()
    baker=models.ForeignKey(Baker,on_delete=models.CASCADE)
    # product_id = models.IntegerField()
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    shape = models.CharField(max_length=45)
    cake_count = models.IntegerField()
    weight = models.CharField(max_length=45)
    tier = models.IntegerField()
    delivery_date = models.DateField()
    delivery_time = models.TimeField()
    wishes = models.CharField(max_length=45)
    total_price = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    delivery_charge = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'order'
