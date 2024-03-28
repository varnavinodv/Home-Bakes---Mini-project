from django.db import models
from customer.models import Customer
from baker.models import Baker

# Create your models here.
class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    # customer_id = models.CharField(max_length=45)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    # baker_id = models.CharField(max_length=45)
    baker=models.ForeignKey(Baker,on_delete=models.CASCADE)
    rating = models.CharField(max_length=45)
    review = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'rating'
