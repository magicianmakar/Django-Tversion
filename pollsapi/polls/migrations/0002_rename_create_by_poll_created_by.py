# Generated by Django 4.2.2 on 2023-06-24 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='create_by',
            new_name='created_by',
        ),
    ]
