# Generated by Django 4.2.4 on 2023-09-15 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='contact',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='payment',
            name='pid',
            field=models.IntegerField(),
        ),
    ]