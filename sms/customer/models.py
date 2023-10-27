from django.db import models

class Customer(models.Model):
    cname = models.CharField(max_length=50)
    cid = models.IntegerField()
    aemail = models.EmailField()
    category = models.CharField(max_length=25)
    contact = models.BigIntegerField()


    class Meta:
        db_table = "Customer_Table"

    def __str__(self):
        return self.cname






class Order(models.Model):
    CAT_CHOICES = (
        ('abstract', 'Abstract'),
        ('technology', 'Technology'),
        ('digital', 'Digital'),
    )

    modelid = models.CharField(max_length=255)
    name_of_product = models.CharField(max_length=255)
    description = models.CharField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    bill = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_purchase = models.DateField()
    category = models.CharField(max_length=20, choices=CAT_CHOICES)

    def __str__(self):
        return self.name_of_product


