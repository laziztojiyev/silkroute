from django.db import models
from django.db.models import CharField, ImageField, DecimalField, DateTimeField, DateField


# Create your models here.
class Packages(models.Model):
    name = CharField(max_length=255)
    image = ImageField(upload_to='media/package_images',
                       blank=True,
                       null=True)
    cost = DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    duration = CharField(max_length=100)
    depart_time = DateField()
    return_time = DateField()
    destination = CharField(max_length=255)

    def __str__(self):
        return self.name
