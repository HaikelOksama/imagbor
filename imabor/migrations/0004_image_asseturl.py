# Generated by Django 3.2.8 on 2021-11-20 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imabor', '0003_image_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='asseturl',
            field=models.TextField(default=''),
        ),
    ]