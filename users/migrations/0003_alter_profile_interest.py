# Generated by Django 4.2.1 on 2023-06-13 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profileimage_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='interest',
            field=models.ManyToManyField(blank=True, related_name='interests', to='users.interest', verbose_name='Interests'),
        ),
    ]
