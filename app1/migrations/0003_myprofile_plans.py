# Generated by Django 4.1.7 on 2023-03-15 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_myprofile_plans'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='Plans',
            field=models.ManyToManyField(to='app1.plan'),
        ),
    ]
