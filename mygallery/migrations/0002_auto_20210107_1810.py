# Generated by Django 3.1.3 on 2021-01-07 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
