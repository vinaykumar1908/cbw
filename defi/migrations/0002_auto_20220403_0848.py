# Generated by Django 3.2.6 on 2022-04-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dpc',
            name='DPCName',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tc',
            name='TCName',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dpcarea',
            name='DPCArea',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dpcdef',
            name='DPCDef',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
