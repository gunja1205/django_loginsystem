from django.db import models

# Create your models here.
class Vaccination_center(models.Model):
    State = models.CharField("Enter State name ", max_length=50)
    District = models.CharField("Enter District name", max_length=50)
    center = models.CharField("Enter Center name", max_length=50)



    class Meta:
        db_table = "centers"