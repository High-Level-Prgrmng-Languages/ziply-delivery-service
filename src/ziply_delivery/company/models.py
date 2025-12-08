from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200, unique=True)
    address = models.TextField()
    zipcode = models.CharField(max_length=10)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    account = models.CharField(max_length=50, unique=True)

    # Optional improvements
    created_at = models.DateTimeField(
        auto_now_add=True)  # set once when created
    updated_at = models.DateTimeField(auto_now=True)      # updates every save
