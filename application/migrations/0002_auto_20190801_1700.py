# Generated by Django 2.2.1 on 2019-08-01 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='zip_code',
            new_name='state_id',
        ),
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
