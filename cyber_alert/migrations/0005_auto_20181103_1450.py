# Generated by Django 2.0.5 on 2018-11-03 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyber_alert', '0004_givertransaction_countone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='givertransaction',
            name='countone',
            field=models.IntegerField(default=0),
        ),
    ]
