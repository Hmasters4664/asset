# Generated by Django 2.2.2 on 2019-06-22 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='department',
        ),
        migrations.AddField(
            model_name='user',
            name='employee_id',
            field=models.CharField(default=1224544, max_length=50, verbose_name='Employee ID'),
            preserve_default=False,
        ),
    ]
