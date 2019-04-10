# Generated by Django 2.1.7 on 2019-04-09 10:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('launch', '0025_remove_item_cuisine'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='success',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='token',
        ),
        migrations.AddField(
            model_name='transaction',
            name='collect_timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='transaction',
            name='order',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='launch.Order'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='orderStatus',
            field=models.CharField(default='Pending', max_length=10),
        ),
        migrations.AddField(
            model_name='transaction',
            name='restaurant',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='launch.Restaurant'),
        ),
    ]
