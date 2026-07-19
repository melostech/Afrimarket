from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ("BUYER", "Buyer"),
        ("SELLER", "Seller"),
        ("ADMIN", "Admin"),
    ]

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default="BUYER",
    )

    def __str__(self):
        return self.username


class SellerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="seller_profile"
    )
    business_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    business_address = models.TextField()
    business_description = models.TextField(blank=True)
    tax_id = models.CharField(max_length=100, blank=True)
    subscription_plan = models.CharField(max_length=50, default="Free")
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name

