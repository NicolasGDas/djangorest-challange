# Generated by Django 4.0.3 on 2022-03-19 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders_details', '0002_alter_orderdetail_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderdetail',
            old_name='Order',
            new_name='order',
        ),
    ]
