# Generated by Django 4.2.5 on 2024-03-19 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locator', '0002_rolpoints_co_ordinator_rolpoints_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rolpoints',
            name='landmarks',
        ),
        migrations.AddField(
            model_name='rolpoints',
            name='date_time',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='rolpoints',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='rolpoints',
            name='region',
            field=models.CharField(max_length=20),
        ),
    ]