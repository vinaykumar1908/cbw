# Generated by Django 3.2.6 on 2022-04-03 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defi', '0004_auto_20220403_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rake',
            name='Name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
