# Generated by Django 4.0.3 on 2022-06-24 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structures', '0001_initial'),
        ('eqrApp', '0016_alter_employee_employee_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='society_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='structures.society', verbose_name='Societé'),
        ),
    ]
