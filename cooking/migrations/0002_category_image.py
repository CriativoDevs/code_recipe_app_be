# Generated by Django 4.2.1 on 2023-06-21 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
