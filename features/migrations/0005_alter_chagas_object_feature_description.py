# Generated by Django 4.0.7 on 2022-11-16 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0004_remove_chagas_object_fold_change_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chagas_object',
            name='feature_description',
            field=models.CharField(max_length=128, null=True),
        ),
    ]