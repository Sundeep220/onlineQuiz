# Generated by Django 4.0.4 on 2022-10-13 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_scoreboard_attempt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scoreboard',
            name='attempt',
        ),
    ]
