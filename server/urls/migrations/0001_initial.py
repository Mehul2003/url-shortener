# Generated by Django 4.1.13 on 2024-01-12 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.CharField(max_length=50)),
                ('endpoint', models.CharField(max_length=500)),
            ],
        ),
    ]
