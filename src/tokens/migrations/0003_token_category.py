# Generated by Django 2.0.4 on 2018-08-19 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0002_tokenfind'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='category',
            field=models.TextField(default='', help_text='The category/hint for this token (physical, website, whatever)'),
            preserve_default=False,
        ),
    ]