# Generated by Django 3.2 on 2021-04-19 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_alter_sale_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='transaction_id',
            field=models.CharField(blank=True, editable=False, max_length=12),
        ),
    ]