# Generated by Django 4.0.7 on 2022-11-08 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pathogen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_name', models.CharField(max_length=100, null=True)),
                ('genbank_id', models.CharField(max_length=100, null=True)),
                ('strain', models.CharField(max_length=100, null=True)),
                ('isolate', models.CharField(max_length=100, null=True)),
                ('host', models.CharField(max_length=100, null=True)),
                ('collection_year', models.IntegerField(null=True)),
                ('collection_date', models.DateField(blank=True, null=True)),
                ('country_sample', models.CharField(max_length=100, null=True)),
                ('geo_loc_name', models.CharField(max_length=100, null=True)),
                ('latitude', models.CharField(max_length=100, null=True)),
                ('longitude', models.CharField(max_length=100, null=True)),
                ('nature_coordinates', models.CharField(max_length=100, null=True)),
                ('host_stage', models.CharField(max_length=100, null=True)),
                ('isolation_source', models.CharField(max_length=100, null=True)),
                ('pool_individual', models.CharField(max_length=100, null=True)),
                ('sample_conservation_method', models.CharField(max_length=100, null=True)),
                ('sequencing_technology', models.CharField(max_length=100, null=True)),
                ('sequencer', models.CharField(max_length=100, null=True)),
                ('additional_info_sequencing', models.CharField(max_length=100, null=True)),
                ('nb_reads', models.IntegerField(null=True)),
                ('seq_coverage', models.IntegerField(null=True)),
                ('seq_size', models.IntegerField(null=True)),
                ('viral_charge', models.CharField(max_length=100, null=True)),
                ('assembly', models.CharField(max_length=100, null=True)),
                ('genome_type', models.CharField(max_length=100, null=True)),
                ('structure', models.CharField(max_length=100, null=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('collected_by', models.CharField(max_length=100, null=True)),
                ('organization', models.CharField(max_length=100, null=True)),
                ('department', models.CharField(max_length=100, null=True)),
                ('country_organization', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('street', models.CharField(max_length=100, null=True)),
                ('postal_code', models.CharField(max_length=100, null=True)),
                ('project_data_type', models.CharField(max_length=100, null=True)),
                ('sample_score', models.CharField(max_length=100, null=True)),
                ('project_title', models.CharField(max_length=100, null=True)),
                ('public_description', models.CharField(max_length=100, null=True)),
                ('ncbi_project', models.CharField(max_length=16, null=True)),
                ('bioproject_id', models.CharField(max_length=16, null=True)),
                ('biosample_id', models.CharField(max_length=100, null=True)),
                ('time_release', models.DateField(null=True)),
                ('date_release', models.DateField(null=True)),
                ('organism', models.CharField(max_length=100, null=True)),
                ('kingdom', models.CharField(max_length=100, null=True)),
                ('doi', models.CharField(max_length=100, null=True)),
                ('notes', models.CharField(max_length=100, null=True)),
                ('project_name', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
