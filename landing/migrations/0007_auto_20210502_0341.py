# Generated by Django 3.1.7 on 2021-05-02 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0006_auto_20210430_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='github_link',
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='information',
            name='gitlab_link',
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='information',
            name='linkedin_link',
            field=models.URLField(blank=True, max_length=300),
        ),
    ]
