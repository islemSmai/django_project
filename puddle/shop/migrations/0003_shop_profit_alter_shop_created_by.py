# Generated by Django 4.2.12 on 2024-05-31 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0002_alter_shop_titre'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='profit',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='shop',
            name='created_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL),
        ),
    ]