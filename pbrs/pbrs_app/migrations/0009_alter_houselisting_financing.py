# Generated by Django 5.0.6 on 2024-07-03 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pbrs_app', '0008_houselisting_financing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houselisting',
            name='financing',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]
