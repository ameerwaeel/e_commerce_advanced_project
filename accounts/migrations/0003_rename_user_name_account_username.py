# Generated by Django 5.1.3 on 2024-12-04 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_is_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='user_name',
            new_name='username',
        ),
    ]
