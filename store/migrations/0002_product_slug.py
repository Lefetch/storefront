# Generated by Django 5.0.6 on 2024-07-10 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='-', unique=True),
            preserve_default=False,
        ),
    ]
