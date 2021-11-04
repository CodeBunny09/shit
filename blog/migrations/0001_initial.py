# Generated by Django 3.2.9 on 2021-11-04 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', models.TextField(blank=True, max_length=10000, null=True)),
                ('about', models.TextField(blank=True, max_length=10000, null=True)),
                ('twitter', models.URLField(blank=True, max_length=100, null=True)),
                ('facebook', models.URLField(blank=True, max_length=100, null=True)),
                ('instagram', models.URLField(blank=True, max_length=100, null=True)),
                ('github', models.URLField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
