from django.db import models

# This file defines the data model (used to setup SQL schema)
# Note: blank attribute set to true by default, enabling empty value

class Chagas_object(models.Model):
    feature_name = models.fields.CharField(max_length=128)
    feature_description = models.fields.CharField(max_length=128, null=True)  
    feature_name_paper = models.fields.CharField(max_length=128)
    feature_id = models.fields.CharField(max_length=128, null=True) 
    feature_type = models.fields.CharField(max_length=128)
    feature_variation = models.fields.CharField(max_length=128, null=True)
    phenotype1 = models.fields.CharField(max_length=128)
    phenotype1_description = models.fields.CharField(max_length=128, null=True)
    phenotype2 = models.fields.CharField(max_length=128)
    phenotype2_description = models.fields.CharField(max_length=128, null=True)
    tissue = models.fields.CharField(max_length=128)
    tissue_description = models.fields.CharField(max_length=128, null=True)
    experimental = models.fields.CharField(max_length=3)
    method = models.fields.CharField(max_length=128, null=True)
    interaction_observed = models.fields.CharField(max_length=3, null=True)
    name_interactive_features = models.fields.CharField(max_length=128, null=True)
    id_interactive_features = models.fields.CharField(max_length=128, null=True)
    type_interactive_features = models.fields.CharField(max_length=128, null=True)
    organism = models.fields.CharField(max_length=128)
    population = models.fields.CharField(max_length=128, null=True)
    tcruzi_strain = models.fields.CharField(max_length=128, null=True)
    pmid = models.fields.CharField(max_length=128)
    doi = models.fields.CharField(max_length=128, null=True)
    paper_title = models.fields.CharField(max_length=255)
    paper_date = models.IntegerField()



    class Meta:
        ordering = ['feature_name']
   
