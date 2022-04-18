# Generated by Django 3.2.2 on 2022-04-11 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('defi', '0019_mcsection_tcsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcremark',
            name='Section',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, related_name='MCSection1', to='defi.mcsection'),
        ),
        migrations.AddField(
            model_name='tcremark',
            name='Section',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, related_name='TCSection1', to='defi.tcsection'),
        ),
    ]