# Generated by Django 4.1.4 on 2023-09-13 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_remove_invoice_paymentterms_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='clientLogo',
        ),
    ]
