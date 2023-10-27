from django.db import models

class Payment(models.Model):
    pid = models.IntegerField()
    pmethod = models.CharField(max_length=30)
    category = models.CharField(max_length=25)
    contact = models.BigIntegerField()

    class Meta:
        db_table = "Payment_Table"

    def __str__(self):
        return str(self.pid)