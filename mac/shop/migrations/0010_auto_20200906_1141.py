# Generated by Django 3.0.8 on 2020-09-06 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200906_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_update',
            name='timestamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]