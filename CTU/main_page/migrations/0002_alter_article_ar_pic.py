# Generated by Django 4.1.4 on 2022-12-19 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='ar_pic',
            field=models.TextField(),
        ),
    ]
