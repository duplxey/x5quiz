# Generated by Django 3.0.2 on 2020-01-24 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_quizuserresult_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentstatistics',
            name='title',
            field=models.CharField(blank=True, default='undefined', max_length=255),
        ),
    ]
