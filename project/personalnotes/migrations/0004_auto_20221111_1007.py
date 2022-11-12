# Generated by Django 3.2.6 on 2022-11-11 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personalnotes', '0003_auto_20221111_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='note_author_id',
        ),
        migrations.AlterField(
            model_name='author',
            name='name_author',
            field=models.CharField(default='unknown', max_length=35, unique=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='note_author_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalnotes.author'),
        ),
    ]
