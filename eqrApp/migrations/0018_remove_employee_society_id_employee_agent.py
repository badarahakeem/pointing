# Generated by Django 4.0.3 on 2022-06-24 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structures', '0001_initial'),
        ('eqrApp', '0017_employee_society_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='society_id',
        ),
        migrations.AddField(
            model_name='employee',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='structures.agent', verbose_name='Agent'),
        ),
    ]
