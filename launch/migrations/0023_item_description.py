# Generated by Django 2.1.7 on 2019-04-08 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launch', '0022_restaurant_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
