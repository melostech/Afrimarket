# core/choices.py
from django.db import models
from django.utils.translation import gettext_lazy as _

class UserRole(models.TextChoices):
    BUYER = "BUYER", _("Buyer")
    SELLER = "SELLER", _("Seller")
    ADMIN = "ADMIN", _("Admin")

class ProductCondition(models.TextChoices):
    NEW = "NEW", _("New")
    USED_LIKE_NEW = "USED_LIKE_NEW", _("Used - Like New")
    USED_GOOD = "USED_GOOD", _("Used - Good")
    USED_FAIR = "USED_FAIR", _("Used - Fair")

class ProductStatus(models.TextChoices):
    AVAILABLE = "AVAILABLE", _("Available")
    RESERVED = "RESERVED", _("Reserved")
    SOLD = "SOLD", _("Sold")
    OUT_OF_STOCK = "OUT_OF_STOCK", _("Out of Stock")
    EXPIRED = "EXPIRED", _("Expired")

class RentalStatus(models.TextChoices):
    AVAILABLE = "AVAILABLE", _("Available")
    RENTED = "RENTED", _("Rented")
    UNAVAILABLE = "UNAVAILABLE", _("Unavailable")

class OrderStatus(models.TextChoices):
    PENDING = "PENDING", _("Pending")
    COMPLETED = "COMPLETED", _("Completed")
    CANCELLED = "CANCELLED", _("Cancelled")

class PaymentStatus(models.TextChoices):
    PENDING = "PENDING", _("Pending")
    SUCCESSFUL = "SUCCESSFUL", _("Successful")
    FAILED = "FAILED", _("Failed")

class PaymentType(models.TextChoices):
    CONTACT_ACCESS = "CONTACT_ACCESS", _("Contact Access")
    SUBSCRIPTION = "SUBSCRIPTION", _("Subscription")

class SubscriptionStatus(models.TextChoices):
    ACTIVE = "ACTIVE", _("Active")
    EXPIRED = "EXPIRED", _("Expired")
    CANCELLED = "CANCELLED", _("Cancelled")
