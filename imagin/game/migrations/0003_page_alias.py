# Generated by Django 3.1.5 on 2021-01-20 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='alias',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
