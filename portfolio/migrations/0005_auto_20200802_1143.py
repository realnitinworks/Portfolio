# Generated by Django 3.0.7 on 2020-08-02 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_certificate_certificategroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificategroup',
            name='slug',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
