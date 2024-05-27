# Generated by Django 5.0.1 on 2024-05-26 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipeProject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=100)),
                ('recipe_description', models.TextField()),
                ('recipe_image', models.ImageField(upload_to='recipe')),
            ],
        ),
        migrations.DeleteModel(
            name='Receipe',
        ),
    ]
