# Generated by Django 4.0.3 on 2023-01-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0005_recipes_ringredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='ringredients',
            field=models.JSONField(default=[]),
        ),
    ]
