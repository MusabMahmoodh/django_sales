# Generated by Django 3.2 on 2021-04-19 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_alter_sale_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
