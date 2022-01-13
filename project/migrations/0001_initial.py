# Generated by Django 3.2.9 on 2021-12-05 06:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('code', models.TextField()),
                ('conclusion', models.TextField()),
            ],
        ),
    ]