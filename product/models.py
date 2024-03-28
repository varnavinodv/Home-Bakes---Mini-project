from django.db import models
from baker.models import Baker
# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    # baker_id = models.IntegerField()
    baker=models.ForeignKey(Baker,on_delete=models.CASCADE)
    cake_name = models.CharField(max_length=45)
    image1 = models.CharField(max_length=200)
    image2 = models.CharField(max_length=200, blank=True, null=True)
    image3 = models.CharField(max_length=200, blank=True, null=True)
    flavour = models.CharField(max_length=45)
    price = models.CharField(max_length=45)
    type = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'product'
