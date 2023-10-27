from django.db import models

class Reports(models.Model):
    rid = models.IntegerField()
    report = models.CharField(max_length=30)
    category = models.CharField(max_length=25)
    aemail = models.EmailField(max_length=100)

    class Meta:
        db_table ="Reports_Table"

    def __str__(self):
        return str(self.rid)