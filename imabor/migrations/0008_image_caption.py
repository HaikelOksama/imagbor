# Generated by Django 3.2.8 on 2021-11-28 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imabor', '0007_remove_image_asseturl'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='caption',
            field=models.CharField(default='high qualitY', max_length=200),
        ),
    ]
