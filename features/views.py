from django.shortcuts import *
from django.apps import apps
from django.http.response import StreamingHttpResponse
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from chagasDB.settings import EMAIL_HOST_USER
from features.models import Chagas_object
from features.filters import ChagasFilters
import os, csv

CHAGAS_VERSION = os.getenv('CHAGAS_VERSION')
                
def home(request):
    return render(request, 'home.html', {})
 
def guide(request):
    return render(request, 'guide.html', {})

def submit(request, **kwargs):
    context = {}
    # Check for error messages
    if 'message' in kwargs :
       context['ctxt_message'] = kwargs.get('message')

    return render(request, 'submit.html', context)

def about(request):
    context = {}
    if CHAGAS_VERSION != None:
        context['version'] = CHAGAS_VERSION
    return render(request, 'about.html', context)

class Echo:
    def write(self, value):
        return value

def database(request):
    # Get all objects and filters them with user choices
    myFilter = ChagasFilters(request=request.GET, queryset=Chagas_object.objects.all()) 
    
    # Paginate the number of results 
    paginator = Paginator(myFilter.qs, 20)
    page = request.GET.get('page')

    # Allow user to switch pages and stay on the filtered dataset
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)

    # Get number of entries information
    nb_objects_all = Chagas_object.objects.all().count()
    nb_objects = paginator.count

    # Get list of options to display for the CharFilter box
    feature_name_options = list(Chagas_object.objects.values_list('feature_name', flat=True).distinct())
    feature_description_options = list(Chagas_object.objects.values_list('feature_description', flat=True).distinct())
    feature_id_options = list(Chagas_object.objects.values_list('feature_id', flat=True).distinct())
    feature_options = feature_name_options + feature_description_options + feature_id_options

    context = {'myFilter':myFilter, 'feature_options':feature_options, 'response':response, 'nb_objects':nb_objects}

    # Get number of entries filtered
    if nb_objects_all != nb_objects:
        nb_filtered = nb_objects_all - nb_objects
        context['nb_filtered'] = nb_filtered

    # Check for last update info
    if CHAGAS_VERSION != None:
        context['version'] = CHAGAS_VERSION

    # Download data
    id_list = request.POST.getlist('boxes')
    if len(id_list) != 0:
        # If all boxes are checked we consider that the user wants to download the current filtered database
        if nb_objects_all == nb_objects: # If no filter is currently applied
            if len(id_list) == 21:
                id_list =  Chagas_object.objects.values_list('id', flat=True)
            elif '0000' in id_list:
                id_list = list(map(int, id_list))
                ids_page = [object.id for object in response.object_list]
                to_pop = list(set(ids_page) - set(id_list))
                id_list = Chagas_object.objects.values_list('id', flat=True).exclude(id__in=to_pop)

        else: # If a filter is applied
            if len(id_list) == 21:
                id_list = [elem.id for elem in myFilter.qs]
            elif '0000' in id_list:
                id_list = list(map(int, id_list))
                ids_page = [object.id for object in response.object_list]
                to_pop = list(set(ids_page) - set(id_list))
                id_list = [elem.id for elem in myFilter.qs if elem.id not in to_pop]
            
        # Open a csv variable with buffer
        echo_buffer = Echo()
        csv_writer = csv.writer(echo_buffer, delimiter ='\t')
        csv_writer.writerow(['feature_name', 'feature_description', 'feature_name_paper', 'feature_id', 'feature_type', 'feature_variation', 'phenotype1', 'phenotype1_description', 'phenotype2', 'phenotype2_description', 'tissue', 'tissue_description', 'experimental', 'method', 'interaction_observed', 'name_interactive_features', 'id_interactive_features', 'type_interactive_features', 'organism', 'population', 'tcruzi_strain', 'pmid', 'doi', 'paper_title', 'paper_date'])

        queryset = Chagas_object.objects.filter(id__in=id_list).values_list('feature_name', 'feature_description', 'feature_name_paper', 'feature_id', 'feature_type', 'feature_variation', 'phenotype1', 'phenotype1_description', 'phenotype2', 'phenotype2_description', 'tissue', 'tissue_description', 'experimental', 'method', 'interaction_observed', 'name_interactive_features', 'id_interactive_features', 'type_interactive_features', 'organism', 'population', 'tcruzi_strain', 'pmid', 'doi', 'paper_title', 'paper_date')
        queryset = list(queryset)

        queryset.insert(0, ("Feature name", "Feature description", "Feature name paper", "Feature ID", "Feature type", "Feature variation", "Phenotype1", "Description phenotype 1", "Phenotype2", "Description phenotype 2", "Tissue",
        "Tissue description", "Experimental", "Method", "Interaction observed", "Name interactive feature", "ID interactive feature", "Type interactive feature", "Organism", "Population", "T.cruzi strain", "Paper PMID",
        "Paper DOI", "Paper title", "Paper publication date"))

        # By using a generator expression to write each row in the queryset
        # python calculates each row as needed, rather than all at once.
        # Note that the generator uses parentheses, instead of square
        # brackets – ( ) instead of [ ].
        rows = (csv_writer.writerow(row) for row in queryset)  # queryset is a list of values

        # Prepare a TSV file to be send
        response = StreamingHttpResponse(rows, content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="Chagas_metadata.tsv"'

        return response    

    return render(request, 'database.html', context)

#Download page
def download(request):
    dl = request.POST.get('dl')
    if dl != None:
        
        echo_buffer = Echo()
        csv_writer = csv.writer(echo_buffer, delimiter ='\t')
        
        queryset = Chagas_object.objects.values_list('feature_name', 'feature_description', 'feature_name_paper', 'feature_id', 'feature_type', 'feature_variation', 'phenotype1', 'phenotype1_description', 'phenotype2', 'phenotype2_description', 'tissue', 'tissue_description', 'experimental', 'method', 'interaction_observed', 'name_interactive_features', 'id_interactive_features', 'type_interactive_features', 'organism', 'population', 'tcruzi_strain', 'pmid', 'doi', 'paper_title', 'paper_date')
        queryset = list(queryset)

        queryset.insert(0, ("Feature name", "Feature description", "Feature name paper", "Feature ID", "Feature type", "Feature variation", "Phenotype1", "Description phenotype 1", "Phenotype2", "Description phenotype 2", "Tissue",
        "Tissue description", "Experimental", "Method", "Interaction observed", "Name interactive feature", "ID interactive feature", "Type interactive feature", "Organism", "Population", "T.cruzi strain", "Paper PMID",
        "Paper DOI", "Paper title", "Paper publication date"))
        
        rows = (csv_writer.writerow(row) for row in queryset)

        response = StreamingHttpResponse(rows, content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="Chagas_metadata.tsv"'

        return response  
        
    return render(request, 'download.html', {})

def send_mail_with_file(request):
    # Get field forms and check if they are filled
    contact_name = request.POST.get('contact_name')
    contact_email = request.POST.get('contact_email')
    contact_message = request.POST.get('contact_message')

    if contact_name.strip() == "" or contact_email.strip() == "":
        return submit(request, message="The submitter name and email must be indicated.")
    else:
        if "@" not in contact_email:
            return submit(request, message="Mail is incorrect.")

    # Create mail
    email = EmailMessage('Data submission from: '+contact_email, 'Name of submitter: '+contact_name+' | Mail: '+contact_email+' | Message: '+contact_message, EMAIL_HOST_USER, to=['pauline.brochet@gmail.com'])
    email.content_subtype = 'html'

    try:
        file = request.FILES['file']
    except Exception:
        return submit(request, message="No attachment file found.")

    # Check if the attachment file size is above 25Mo 
    if file.size >= 25000000:
        return submit(request, message="Attachment file too heavy (>25Mo).")

    # Attach and send mail
    email.attach(file.name, file.read(), file.content_type)
    email.send()

    return submit(request, message="File sent. Thank you!")

