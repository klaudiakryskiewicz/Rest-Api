# Generated by Django 3.0.9 on 2020-08-05 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0003_auto_20200805_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='average_rating',
            field=models.FloatField(null=True),
        ),
    ]
