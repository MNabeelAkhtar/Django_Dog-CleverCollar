# Generated by Django 4.1.4 on 2022-12-11 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_post_image_alter_post_mor_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='mor_image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='sec_image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
