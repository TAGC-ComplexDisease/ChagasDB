# Generated by Django 4.0.7 on 2022-11-21 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0005_alter_chagas_object_feature_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chagas_object',
            options={'ordering': ['feature_name']},
        ),
    ]
