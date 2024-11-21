# Generated by Django 4.2.1 on 2023-06-19 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('excerpt', models.CharField(default='', max_length=255)),
                ('content', models.TextField(blank=True, null=True)),
                ('contentTwo', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image')),
                ('ingredients', models.TextField(blank=True, null=True)),
                ('post_label', models.CharField(blank=True, choices=[('POPULAR', 'popular')], max_length=100, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cooking.category')),
            ],
        ),
    ]
