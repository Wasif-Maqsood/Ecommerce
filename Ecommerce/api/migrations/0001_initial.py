# Generated by Django 4.2.4 on 2023-09-06 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Product_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Product_Name', models.CharField(max_length=30)),
            ],
        ),
    ]