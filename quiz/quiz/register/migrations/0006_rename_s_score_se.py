# Generated by Django 4.0.4 on 2022-08-11 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_score'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='s',
            new_name='se',
        ),
    ]
