# Generated by Django 3.1.5 on 2021-01-23 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_images_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('message', models.TextField()),
            ],
        ),
    ]
