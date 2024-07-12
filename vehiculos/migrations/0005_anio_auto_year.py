# Generated by Django 5.0.6 on 2024-07-10 23:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0004_remove_product_category_remove_pricehistory_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='auto',
            name='year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='anios', to='vehiculos.anio'),
        ),
    ]
