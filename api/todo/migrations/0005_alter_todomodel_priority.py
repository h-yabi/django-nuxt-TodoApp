# Generated by Django 3.2.6 on 2021-09-12 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_todomodel_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(choices=[('Low', 'Low'), ('Middle', 'Middle'), ('High', 'High')], max_length=10),
        ),
    ]
