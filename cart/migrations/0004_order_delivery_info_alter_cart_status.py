# Generated by Django 5.0.3 on 2024-04-29 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_ordercart_is_review'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.delivery'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
