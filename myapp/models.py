from django.db import models

# Create your models here.
class Person(models.Model):
    def __str__(self):
        return self.first_name
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    image = models.CharField(max_length=500,default="https://cdn.patch.com/assets/contrib/images/placeholder-user-photo.png")
