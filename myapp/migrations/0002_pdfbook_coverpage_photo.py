# Generated by Django 3.1.3 on 2021-04-22 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfbook',
            name='coverpage_photo',
            field=models.ImageField(default='image.png', upload_to='images/'),
        ),
    ]