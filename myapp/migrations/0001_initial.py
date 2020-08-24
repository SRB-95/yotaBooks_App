# Generated by Django 3.1 on 2020-08-23 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
            ],
        ),
    ]
