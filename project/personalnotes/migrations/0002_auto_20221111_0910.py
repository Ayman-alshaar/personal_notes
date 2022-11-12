# Generated by Django 3.2.6 on 2022-11-11 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personalnotes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('note_id', models.AutoField(primary_key=True, serialize=False)),
                ('note_title', models.CharField(default='unknown', max_length=35)),
                ('Note_content', models.TextField()),
                ('date_created_note', models.DateField()),
            ],
            options={
                'verbose_name': 'name',
            },
        ),
        migrations.DeleteModel(
            name='Author1',
        ),
        migrations.AlterField(
            model_name='author',
            name='age_author',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='author',
            name='mobile_number',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='note',
            name='note_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalnotes.author'),
        ),
    ]