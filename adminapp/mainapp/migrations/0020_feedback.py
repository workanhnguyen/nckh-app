# Generated by Django 4.1.5 on 2023-02-10 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_universitie'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
                ('content', models.TextField(blank=True)),
            ],
        ),
    ]
