# Generated by Django 4.0.7 on 2022-11-08 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0002_chagas_object_delete_pathogen'),
    ]

    operations = [
        migrations.AddField(
            model_name='chagas_object',
            name='doi',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='chagas_object',
            name='paper_title',
            field=models.CharField(max_length=255),
        ),
    ]
