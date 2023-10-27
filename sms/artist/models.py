from django.db import models
from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus

class Artist(models.Model):
  name = models.CharField(max_length = 100)
  aemail = models.EmailField()
  category = models.CharField(max_length = 25)


  def __str__(self):
        return self.name



class Persons(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    COUNTRY_CHOICES = [
        ('US', 'United States'),
        ('CA', 'Canada'),
        ('UK', 'United Kingdom'),
        ('AU', 'Australia'),
        ('JP', 'Japan'),
        ('IN','India'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    interest = models.CharField(max_length=100)
    country = models.CharField(max_length=100,choices=COUNTRY_CHOICES)

    class Meta:
        db_table = "Person_Table"
    def __str__(self):
        return self.name







class Order(models.Model):
    objects = None
    name = CharField(_("Customer Name"), max_length=254, blank=False, null=False)
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    status = CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"


