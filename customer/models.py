from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    age = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    phone_no = models.CharField(max_length=45)
    house_name = models.CharField(max_length=45)
    post_office = models.CharField(max_length=45)
    pin_code = models.CharField(max_length=45)
    district = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'customer'