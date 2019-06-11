# Generated by Django 2.0.5 on 2018-11-03 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cyber_alert', '0005_auto_20181103_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sendquery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sendquery', models.CharField(max_length=400)),
                ('transid', models.ForeignKey(on_delete='cascade', to='cyber_alert.GiverTransaction')),
            ],
        ),
    ]
