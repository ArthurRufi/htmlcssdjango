# Generated by Django 4.2.2 on 2023-07-19 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_rename_desc_recipe_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='preparetion_steps',
            new_name='preparation_steps',
        ),
    ]