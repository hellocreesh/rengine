# Generated by Django 3.2.4 on 2021-12-07 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanEngine', '0004_auto_20211207_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='installedexternaltool',
            name='update_command',
            field=models.CharField(default='test', max_length=150),
            preserve_default=False,
        ),
    ]
