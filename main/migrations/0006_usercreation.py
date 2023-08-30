# Generated by Django 4.2.4 on 2023-08-09 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_sale_sale_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCreation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('nationality', models.TextField()),
                ('date_of_birth', models.DateField(auto_now=True)),
            ],
        ),
    ]