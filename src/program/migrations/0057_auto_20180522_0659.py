# Generated by Django 2.0.4 on 2018-05-22 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0056_add_urltypes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urltype',
            name='icon',
            field=models.CharField(default='link', help_text="Name of the fontawesome icon to use without the 'fa-' part", max_length=100),
        ),
    ]
