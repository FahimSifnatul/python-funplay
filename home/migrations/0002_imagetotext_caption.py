# Generated by Django 3.2.4 on 2021-08-10 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagetotext',
            name='caption',
            field=models.CharField(default=0, max_length=100),
        ),
    ]