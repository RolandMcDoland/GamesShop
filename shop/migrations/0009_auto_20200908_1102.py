# Generated by Django 3.0.8 on 2020-09-08 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_offer_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=models.TextField(),
        ),
    ]