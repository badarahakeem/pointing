# Generated by Django 4.0.3 on 2022-06-02 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eqrApp', '0007_pointing'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointing',
            name='clock_out',
            field=models.DateTimeField(blank=True, null=True, verbose_name='pointage fin'),
        ),
        migrations.AlterField(
            model_name='pointing',
            name='clock_time',
            field=models.DateTimeField(verbose_name='pointage debut'),
        ),
    ]
