from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title=models.CharField(max_length=64)
    desc=models.TextField()
    bid=models.DecimalField(max_digits=10,decimal_places=2)
    url=models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    category=models.CharField(max_length=64,blank=True,choices=[
        ("Fashion", "Fashion"),
        ("Toys", "Toys"),
        ("Electronics", "Electronics"),
        ("Home", "Home"),
        ]
    )
    def __str__(self):
        return f"{self.category} : {self.title}"
    