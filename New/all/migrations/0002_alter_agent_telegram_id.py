# Generated by Django 4.0 on 2021-12-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='telegram_id',
            field=models.BigIntegerField(unique=True, verbose_name='AGENT IDsi'),
        ),
    ]
