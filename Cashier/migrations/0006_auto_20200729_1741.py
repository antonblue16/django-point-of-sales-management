# Generated by Django 3.0.3 on 2020-07-29 10:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Cashier', '0005_auto_20200729_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashierpos',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
