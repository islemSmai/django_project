# Generated by Django 4.2.12 on 2024-05-09 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='titre',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]