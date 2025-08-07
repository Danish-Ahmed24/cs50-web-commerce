from turtle import mode, title
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Bid(models.Model):
    amount = models.DecimalField(max_digits=20,decimal_places=2)
    bidmaker = models.ForeignKey("User", on_delete=models.CASCADE)
    listing = models.ForeignKey("Listing", on_delete=models.CASCADE, related_name="bids")

    def __str__(self) -> str:
        return f"{self.listing } : {self.bidmaker} , {self.amount}"


class Comment(models.Model):
    text = models.CharField(max_length=128)
    commenter = models.ForeignKey("User", on_delete=models.CASCADE)
    listing = models.ForeignKey("Listing", on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"{self.commenter}: {self.text}"


class Listing(models.Model):
    title=models.CharField(max_length=64)
    desc=models.TextField()
    url=models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey("User", on_delete=models.CASCADE)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="won_listings")
    category=models.CharField(max_length=64,blank=True,choices=[
        ("Fashion", "Fashion"),
        ("Toys", "Toys"),
        ("Electronics", "Electronics"),
        ("Home", "Home"),
        ]
    )


    def __str__(self):
        return f"{self.category} : {self.title}"
    
class WishList(models.Model):
    #data
    listings = models.ManyToManyField(Listing)
    #owner
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"Wishlist of {self.user.username}"
