# Generated by Django 3.2.2 on 2022-04-29 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mnp', '0008_alter_mnp_updatedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mnpsection',
            name='Section',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]