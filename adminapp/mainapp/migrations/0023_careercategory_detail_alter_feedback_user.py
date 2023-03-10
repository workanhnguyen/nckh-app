# Generated by Django 4.1.5 on 2023-02-13 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_university_image_alter_careercategory_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='careercategory',
            name='detail',
            field=models.TextField(default=int),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='feedbacks', to=settings.AUTH_USER_MODEL),
        ),
    ]
