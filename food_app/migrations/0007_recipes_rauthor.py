# Generated by Django 4.0.3 on 2023-01-06 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food_app', '0006_alter_recipes_ringredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='rauthor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
