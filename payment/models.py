from django.db import models
from customer.models import Customer
from baker.models import Baker
from order.models import Order
from thorder.models import Theme

# Create your models here.
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    # customer_id = models.IntegerField()
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    # baker_id = models.IntegerField()
    baker=models.ForeignKey(Baker,on_delete=models.CASCADE)
    # order_id = models.IntegerField(blank=True, null=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    card_holder = models.CharField(max_length=45)
    cvv = models.CharField(max_length=45)
    date = models.DateField()
    amount = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'payment'



class Thpayment(models.Model):
    thpayment_id = models.AutoField(primary_key=True)
    # customer_id = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    # baker_id = models.IntegerField()
    baker = models.ForeignKey(Baker,on_delete=models.CASCADE)
    # theme_id = models.IntegerField()
    theme = models.ForeignKey(Theme,on_delete=models.CASCADE)
    card_holder = models.CharField(max_length=45)
    cvv = models.CharField(max_length=45)
    date = models.DateField()
    amount = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'thpayment'


