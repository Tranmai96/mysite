# Generated by Django 3.0.6 on 2020-05-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('合格', '合格')], max_length=200, null=True),
        ),
    ]
