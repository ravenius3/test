# Generated by Django 3.2.2 on 2023-06-14 14:23

from django.db import migrations, models
import vault.models


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0028_alter_password_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='password',
            field=models.CharField(default=vault.models.pass_gen, max_length=100),
        ),
    ]