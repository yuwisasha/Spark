# Generated by Django 4.2.1 on 2023-05-31 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='Email address')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Is admin')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Interest')),
            ],
            options={
                'verbose_name': 'Interest',
                'verbose_name_plural': 'Interests',
            },
        ),
        migrations.CreateModel(
            name='ProfileImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=users.models.user_directory_path, verbose_name='Photo')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('date_of_birth', models.DateField(verbose_name='Date of birth')),
                ('gender', models.IntegerField(choices=[(None, '(Unknown)'), (0, 'Male'), (1, 'Female')], verbose_name='Gender')),
                ('looking_for', models.IntegerField(choices=[(None, '(Unknown)'), (0, 'Men'), (1, 'Women'), (2, 'Both')], verbose_name='Looking for')),
                ('sexual_identity', models.CharField(choices=[('H', 'Hetero'), ('G', 'Gay'), ('L', 'Lesbian'), ('B', 'Bisexual'), ('A', 'Asexual'), ('D', 'Demisexual'), ('P', 'Pansexual'), ('Q', 'Queer'), ('U', 'Undecided')], max_length=1, verbose_name='Sexual identity')),
                ('bio', models.CharField(blank=True, max_length=200, verbose_name='About')),
                ('interest', models.ManyToManyField(blank=True, to='users.interest', verbose_name='Interests')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Profile')),
            ],
        ),
    ]
