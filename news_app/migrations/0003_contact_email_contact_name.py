# Generated by Django 4.0 on 2023-12-21 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_contact_alter_news_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
