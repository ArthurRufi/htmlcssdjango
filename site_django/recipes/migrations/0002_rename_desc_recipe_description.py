# Generated by Django 4.2.2 on 2023-07-18 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='desc',
            new_name='description',
        ),
    ]
