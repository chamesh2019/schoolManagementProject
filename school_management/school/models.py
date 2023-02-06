from django.db import models


# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=255)
    start_date = models.CharField(max_length=255)
    badge_id = models.CharField(max_length=100)  # link id of badge image
