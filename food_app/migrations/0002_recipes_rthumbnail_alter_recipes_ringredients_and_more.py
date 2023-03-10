# Generated by Django 4.0.3 on 2022-12-30 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='rthumbnail',
            field=models.ImageField(default=None, upload_to='Image'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='ringredients',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='rstep1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='rstep2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='rstep3',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='rstep4',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='rstep5',
            field=models.TextField(),
        ),
    ]
