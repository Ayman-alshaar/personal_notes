# Generated by Django 3.2.6 on 2022-11-11 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalnotes', '0006_note_note_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name_author',
            field=models.CharField(default='unknown', max_length=35),
        ),
    ]
