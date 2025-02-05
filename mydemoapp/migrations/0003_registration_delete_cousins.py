# Generated by Django 5.0.3 on 2024-03-21 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydemoapp', '0002_cousins_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='cousins',
        ),
    ]
