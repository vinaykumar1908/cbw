# Generated by Django 3.2.6 on 2022-04-04 12:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('defi', '0007_auto_20220404_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='MCArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MCArea', models.CharField(blank=True, max_length=100, null=True)),
                ('Date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='MCDef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MCDef', models.CharField(blank=True, max_length=100, null=True)),
                ('Date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='MCRemark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('MCDef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MCDef1', to='defi.mcdef')),
                ('MCDefArea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MCArea1', to='defi.mcarea')),
                ('MCName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MCName1', to='defi.mc')),
            ],
        ),
    ]
