# Generated by Django 3.2.8 on 2021-11-20 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imabor', '0004_image_asseturl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='asseturl',
            field=models.TextField(default='', null=True),
        ),
    ]