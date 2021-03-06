# Generated by Django 3.1 on 2020-08-08 20:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alpha_two_code', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=2)),
                ('domain', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=2)),
                ('web_page', models.CharField(max_length=2)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
