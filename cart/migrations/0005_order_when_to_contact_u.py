# Generated by Django 3.0.1 on 2020-02-06 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_remove_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='when_to_contact_u',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
