# Generated by Django 4.0.7 on 2022-11-08 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chagas_object',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=128)),
                ('feature_description', models.CharField(max_length=128)),
                ('feature_name_paper', models.CharField(max_length=128)),
                ('feature_id', models.CharField(max_length=128, null=True)),
                ('feature_type', models.CharField(max_length=128)),
                ('fold_change', models.CharField(max_length=4, null=True)),
                ('phenotype1', models.CharField(max_length=128)),
                ('phenotype1_description', models.CharField(max_length=128, null=True)),
                ('phenotype2', models.CharField(max_length=128)),
                ('phenotype2_description', models.CharField(max_length=128, null=True)),
                ('tissue', models.CharField(max_length=128)),
                ('tissue_description', models.CharField(max_length=128, null=True)),
                ('experimental', models.CharField(max_length=3)),
                ('method', models.CharField(max_length=128, null=True)),
                ('interaction_observed', models.CharField(max_length=3, null=True)),
                ('name_interactive_features', models.CharField(max_length=128, null=True)),
                ('id_interactive_features', models.CharField(max_length=128, null=True)),
                ('type_interactive_features', models.CharField(max_length=128, null=True)),
                ('organism', models.CharField(max_length=128)),
                ('population', models.CharField(max_length=128, null=True)),
                ('tcruzi_strain', models.CharField(max_length=128, null=True)),
                ('pmid', models.CharField(max_length=128)),
                ('paper_title', models.CharField(max_length=128)),
                ('paper_date', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Pathogen',
        ),
    ]
