# Generated by Django 5.0.3 on 2024-03-22 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydemoapp', '0006_delete_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_file', models.FileField(upload_to='')),
                ('info_file', models.FileField(upload_to='')),
            ],
        ),
    ]
