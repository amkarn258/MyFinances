# Generated by Django 5.0.4 on 2024-05-30 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0034_invoice_client_email_quotaincreaserequest_reason_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="contact_method",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
