# Generated by Django 2.1.4 on 2018-12-20 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='activate',
            new_name='active',
        ),
    ]
