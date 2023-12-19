# Generated by Django 4.2.7 on 2023-12-16 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
