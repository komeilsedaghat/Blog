# Generated by Django 3.2.7 on 2021-10-29 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_special_article',
            field=models.BooleanField(default=False),
        ),
    ]
