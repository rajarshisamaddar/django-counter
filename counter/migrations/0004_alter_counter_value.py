# Generated by Django 5.0.1 on 2024-02-04 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0003_alter_counter_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='value',
            field=models.IntegerField(default=50),
        ),
    ]
