# Generated by Django 4.2.4 on 2023-10-10 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0004_qrcodemodel_delete_qrcodeentry'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QRCodeModel',
        ),
        migrations.AlterModelTable(
            name='artist',
            table=None,
        ),
    ]
