# Generated by Django 3.0.3 on 2020-07-26 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cashier', '0003_auto_20200726_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outpos',
            name='nominal',
            field=models.DecimalField(decimal_places=0, max_digits=15),
        ),
    ]
