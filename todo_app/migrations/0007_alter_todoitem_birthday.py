# Generated by Django 3.2.9 on 2022-06-07 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0006_todoitem_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='birthday',
            field=models.CharField(max_length=100),
        ),
    ]
