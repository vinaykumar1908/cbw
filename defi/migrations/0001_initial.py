# Generated by Django 3.2.6 on 2022-04-03 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DPCArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DPCArea', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DPCDef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DPCDef', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('upload', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RakeName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RTC', to='defi.rake')),
            ],
        ),
        migrations.CreateModel(
            name='DPC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RakeName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RDPC', to='defi.rake')),
            ],
        ),
    ]
