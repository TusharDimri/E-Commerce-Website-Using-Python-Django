# Generated by Django 3.0.8 on 2020-09-05 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_order_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Update',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField()),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
