# Generated by Django 5.2 on 2025-04-14 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('contact', models.TextField(max_length=40)),
                ('number', models.CharField(max_length=10)),
            ],
        ),
    ]
