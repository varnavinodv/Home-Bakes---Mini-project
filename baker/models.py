from django.db import models

# Create your models here.
class Baker(models.Model):
    baker_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    age = models.IntegerField()
    phone_no = models.CharField(max_length=45)
    house_name = models.CharField(max_length=45)
    post_office = models.CharField(max_length=45)
    pin_code = models.CharField(max_length=45)
    district = models.CharField(max_length=45)
    liscense = models.CharField(max_length=200)
    password = models.CharField(max_length=45)
    status = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'baker'

