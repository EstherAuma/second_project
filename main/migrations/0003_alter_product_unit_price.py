# Generated by Django 4.2.4 on 2023-08-06 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_sale_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.PositiveIntegerField(),
        ),
    ]
