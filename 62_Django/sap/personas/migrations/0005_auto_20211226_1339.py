# Generated by Django 3.2.10 on 2021-12-26 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0004_domicilio_no_calle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domicilio',
            name='no_calle',
        ),
        migrations.AddField(
            model_name='domicilio',
            name='num_calle',
            field=models.IntegerField(default=0),
        ),
    ]
