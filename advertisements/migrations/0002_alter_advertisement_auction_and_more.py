# Generated by Django 4.2.3 on 2023-08-04 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='auction',
            field=models.BooleanField(help_text='Отметьте, если торг уместен.obj = AD'),
        ),
        migrations.AlterModelTable(
            name='advertisement',
            table='advertisement',
        ),
    ]
