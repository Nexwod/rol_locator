# Generated by Django 4.2.5 on 2024-03-19 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0003_remove_rolpoints_landmarks_rolpoints_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rolpoints',
            name='image',
            field=models.ImageField(blank=True, upload_to='google_map_image'),
        ),
    ]