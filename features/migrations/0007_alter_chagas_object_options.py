# Generated by Django 4.0.7 on 2022-12-15 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0006_alter_chagas_object_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chagas_object',
            options={'ordering': ['-paper_date']},
        ),
    ]
