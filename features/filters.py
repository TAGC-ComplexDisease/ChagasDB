from django_filters import *
from features.models import Chagas_object
from django_filters.widgets import RangeWidget
from django.db.models import Q, Min, Max
from django import forms

def ChagasFilters(**kwargs):

    request = kwargs.pop('request')
    queryset = kwargs.pop('queryset') 

    # Function to get the list of distinct values in a field of the table. We also get None values to do reverse research. 
    def getChoices(attribute):  
        CHOICES = []
        for i in list(Chagas_object.objects.values_list(attribute, flat=True).distinct().order_by(attribute)):
            CHOICES.append((i,i))
        
        # We want to give the user the possibity to filter on the two phenotypes values at the same time
        if attribute =='phenotype1':
            for i in list(Chagas_object.objects.values_list('phenotype2', flat=True).distinct().order_by('phenotype2')):
                CHOICES.append((i,i))
            CHOICES = set(CHOICES) # Get rid of duplicates

        return CHOICES
    
    # Class to automatically put the min and max values possible in the placeholder of the box of the RangeFilter
    class MyRangeWidget(RangeWidget):
        def __init__(self, attrs=None):
            super().__init__(attrs)
            x = Chagas_object.objects.aggregate(Min('paper_date'))
            y = Chagas_object.objects.aggregate(Max('paper_date'))
            self.widgets[0].attrs.update({'placeholder': x['paper_date__min']})
            self.widgets[1].attrs.update({'placeholder': y['paper_date__max']})
            self.widgets[0].attrs.update({'size': 4}) # Size of input box
            self.widgets[1].attrs.update({'size': 4})

    # Class to define the filters we want to create
    class Filters(FilterSet):
        # We place this filter first because he has an hard query, making it that we need to re-filter afterwards
        phenotype = MultipleChoiceFilter(method='phenotype_custom_filter', label="Phenotype", choices=getChoices('phenotype1'), widget=forms.CheckboxSelectMultiple()) # We call the function below to filters objects on the two phenotype fields
        def phenotype_custom_filter(self, queryset, name, value):
            list_ids = []
            for element in value:
                list_ids = list_ids + list(Chagas_object.objects.filter(phenotype1__exact=element).values_list('id', flat=True))
                list_ids = list_ids + list(Chagas_object.objects.filter(phenotype2__exact=element).values_list('id', flat=True))

            queryset = Chagas_object.objects.filter(id__in=list_ids)
            return queryset

        # CharFilter where the user input is matched against the table field (value contained; case insensitive)
        multifilter = CharFilter(method='multifilter_method', widget=forms.TextInput(attrs={'list':'feature_options','placeholder':'Enter a gene name, description or Ensembl ID...','class':'m-2 rounded-lg border-2 border-orange-700 bg-white w-[900px] p-2 text-normal focus:outline-none'}))
        def multifilter_method(self, queryset, name, value):
            return queryset.filter(
                Q(feature_name__icontains=value) | Q(feature_description__icontains=value) | Q(feature_id__icontains=value)
            )
        
        # ChoiceFilter to give categorical choice to the user based on values in the table field
        feature_type = MultipleChoiceFilter(field_name='feature_type', choices=getChoices('feature_type'), widget=forms.CheckboxSelectMultiple())
        feature_variation = MultipleChoiceFilter(field_name='feature_variation', choices=getChoices('feature_variation'), widget=forms.CheckboxSelectMultiple())
            
        tissue = MultipleChoiceFilter(field_name='tissue', choices=getChoices('tissue'), widget=forms.CheckboxSelectMultiple())
        experimental = MultipleChoiceFilter(field_name='experimental', choices=getChoices('experimental'), widget=forms.CheckboxSelectMultiple())
        interaction_observed = MultipleChoiceFilter(field_name='interaction_observed', choices=getChoices('interaction_observed'), widget=forms.CheckboxSelectMultiple())
        organism = MultipleChoiceFilter(field_name='organism', choices=getChoices('organism'), widget=forms.CheckboxSelectMultiple())
        
        # RangeFilter for the user to select a min or max date of the paper release
        paper_date = RangeFilter(label='Paper date range', widget=MyRangeWidget)

    # Class to define filters self parameters 
    class Meta:
        model = Chagas_object
        ordering = ['-paper_date']
        fields = {'multifilter', 'feature_type','feature_variation','phenotype','tissue','experimental','interaction_observed','organism','paper_date'}

    return Filters(request, queryset)