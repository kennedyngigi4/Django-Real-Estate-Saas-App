# Generated by Django 4.0 on 2023-07-03 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_alter_property_bathrooms_alter_property_bedrooms_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='total_units',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
