# Generated by Django 3.2.8 on 2021-12-22 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_muted'),
    ]

    operations = [
        migrations.AddField(
            model_name='muted',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]
