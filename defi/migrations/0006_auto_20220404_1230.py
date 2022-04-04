# Generated by Django 3.2.6 on 2022-04-04 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('defi', '0005_alter_rake_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MCName', models.CharField(max_length=100)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mcauth', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='dpc',
            name='RakeName',
        ),
        migrations.RemoveField(
            model_name='tc',
            name='RakeName',
        ),
        migrations.AddField(
            model_name='dpc',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='dpcauth', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tc',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tcauth', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Rake',
        ),
    ]
