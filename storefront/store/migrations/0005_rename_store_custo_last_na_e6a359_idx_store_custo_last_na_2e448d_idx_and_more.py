# Generated by Django 4.2.16 on 2024-09-25 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_customer_store_custo_last_na_e6a359_idx_and_more'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='customer',
            new_name='store_custo_last_na_2e448d_idx',
            old_name='store_custo_last_na_e6a359_idx',
        ),
        migrations.AlterModelTable(
            name='customer',
            table='store_customer',
        ),
    ]
