# Generated by Django 5.0.6 on 2024-07-11 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0008_auto_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
