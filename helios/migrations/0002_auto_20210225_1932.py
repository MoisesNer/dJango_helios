# Generated by Django 3.1.7 on 2021-02-25 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publised',
            new_name='publish',
        ),
    ]
