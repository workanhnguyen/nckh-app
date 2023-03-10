# Generated by Django 4.1.5 on 2023-01-27 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_careercategory_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='day_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='career_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answers', to='mainapp.careercategory'),
        ),
    ]
