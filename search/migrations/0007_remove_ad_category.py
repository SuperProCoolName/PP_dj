# Generated by Django 5.0.4 on 2024-06-01 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_ad_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='category',
        ),
    ]
