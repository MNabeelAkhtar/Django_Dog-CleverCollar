# Generated by Django 4.1.4 on 2022-12-10 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_post_age_post_breed_post_mor_image_post_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='mor_image',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='sec_image',
            field=models.CharField(default=None, max_length=250),
        ),
    ]
