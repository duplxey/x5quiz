# Generated by Django 3.0.2 on 2020-01-24 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20200124_0837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizanswer',
            old_name='content',
            new_name='text',
        ),
    ]
