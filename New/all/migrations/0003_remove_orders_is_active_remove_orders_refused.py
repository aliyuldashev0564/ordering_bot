# Generated by Django 4.0.1 on 2022-01-15 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('all', '0002_alter_agent_telegram_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='refused',
        ),
    ]
