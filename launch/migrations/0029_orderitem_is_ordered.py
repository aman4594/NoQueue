# Generated by Django 2.1.7 on 2019-04-10 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launch', '0028_auto_20190409_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='is_ordered',
            field=models.BooleanField(default=False),
        ),
    ]
