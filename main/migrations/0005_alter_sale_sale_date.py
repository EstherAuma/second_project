# Generated by Django 4.2.4 on 2023-08-09 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_product_part_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='sale_date',
            field=models.DateTimeField(),
        ),
    ]
