from django.db import models

# Create your models here.
class Type(models.Model):
    type_clothing = models.CharField(max_length = 10)

    def __str__(self):
        return self.type_clothing