# Generated by Django 3.0.3 on 2020-07-29 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cashier', '0004_auto_20200726_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashierpos',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]