# Generated by Django 2.2.4 on 2019-09-08 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190908_1830'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userdata',
            options={},
        ),
        migrations.AlterModelManagers(
            name='userdata',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='username',
        ),
    ]
