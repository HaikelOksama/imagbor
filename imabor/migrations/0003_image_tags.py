# Generated by Django 3.2.8 on 2021-11-20 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imabor', '0002_alter_image_urls'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='tags',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
