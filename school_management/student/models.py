from django.db import models


# Create your models here.
class Student(models.Model):
    index_number = models.CharField(max_length=20)
    full_name = models.CharField(max_length=255)
    birth_of_date = models.DateField()
    image_id = models.CharField(max_length=20)
    sex = models.CharField(max_length=2)
    nfc_identifier = models.CharField(max_length=255)
    address = models.TextField(max_length=1000)
    parent_id = models.ForeignKey(
        'ParentInfo', on_delete=models.CASCADE
    )


class ParentInfo(models.Model):
    id_number = models.CharField(max_length=15)
    full_name = models.CharField(max_length=255)
    birth_of_date = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=12)
