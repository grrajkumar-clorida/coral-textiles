# Generated by Django 4.2.16 on 2024-10-17 03:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='production',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Done', 'Done'), ('Due', 'Due')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='production',
            name='fabric',
            field=models.CharField(choices=[('Cotton', 'Cotton'), ('Silk', 'Silk'), ('Wool', 'Wool'), ('Polyester', 'Polyester'), ('40 S + 20 D', '40 S + 20 D'), ('34 S + 20 D', '34 S + 20 D'), ('30 S + 40 D', '30 S + 40 D'), ('HELPER', 'HELPER'), ('SERVICE', 'HELPER')], max_length=50),
        ),
    ]
