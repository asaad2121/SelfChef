# Generated by Django 4.0.3 on 2023-01-04 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0003_delete_userdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='ringredients',
        ),
    ]
