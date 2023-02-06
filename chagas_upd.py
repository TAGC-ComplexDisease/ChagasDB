import os, typer
from pathlib import Path

# Setup to launch the script in the django project environment without going through the project python shell
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chagasDB.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Define the CLI options
def main(
    file: Path = typer.Option("", help="Path to a tab separated metadata file."),
    overwrite: bool = typer.Option(False, "--overwrite", help="Use with precaution ! Rewrite the database."),
    ):

    if not os.path.exists(file) or file == Path('.'):
        typer.echo("Path to the chagas metadata file missing (--file).")
    else:
        if overwrite :
            while(True):
                safety = typer.prompt("/!\ You are going to rewrite the current database. Are you sure to proceed ? [yes/no]\n")
                if safety == "yes":
                    upd_data(str(file), overwrite)
                    return
                elif safety == "no":
                    typer.echo("Command aborted.")
                    return
                else:
                    continue 
        else:
            upd_data(str(file), overwrite)
            return

# Function to update the database
from features.models import Chagas_object
from django.core.exceptions import ValidationError
import csv

def upd_data(file, overwrite):
    # Check if the file has the correct number of columns and a correct header
    with open(file, 'r', encoding='latin1') as f:
        reader = next(csv.reader(f, delimiter='\t'))
        if len(reader) != 25:
            typer.echo("Number of columns in the file seems wrong. Are you sure it is tab delimited ?\n")
            return

        correct_header = ["Feature name", "Feature description", "Feature name paper", "Feature ID", "Feature type", "Feature variation", "Phenotype1", "Description phenotype 1", "Phenotype2", "Description phenotype 2", "Tissue",
        "Tissue description", "Experimental", "Method", "Interaction observed", "Name interactive feature", "ID interactive feature", "Type interactive feature", "Organism", "Population", "T.cruzi strain", "Paper PMID",
        "Paper DOI", "Paper title", "Paper publication date"]
        for cell in range(len(reader)):
            result =  all(elem in reader[cell].lower().split(" ") for elem in correct_header[cell].lower().split(" ")) # Check is the header cell contains all the element of the corresponding cell in the list correct_header
            if not result:
                print("The column", reader[cell], "header name doesn't match with the registered name:", correct_header[cell])
                return
    f.close()
    
    # Delete the current DB if the option overwrite is used
    if overwrite == True :
       Chagas_object.objects.all().delete()
    
    duplicate = 0
    added = 0
    failed = 0
    try:
        with open(file, 'r', encoding='latin1') as f:
            reader = csv.reader(f, delimiter='\t')

                                 #    0              1                        2                        3           4               5              6               7                      8               9                   10                  11           12              13               14                          15                         16                          17                  18            19              20          21      22         23           24
            object_attributes = ['feature_name', 'feature_description', 'feature_name_paper', 'feature_id', 'feature_type', 'feature_variation', 'phenotype1', 'phenotype1_description', 'phenotype2', 'phenotype2_description', 'tissue', 'tissue_description', 'experimental', 'method', 'interaction_observed', 'name_interactive_features', 'id_interactive_features', 'type_interactive_features', 'organism', 'population', 'tcruzi_strain', 'pmid', 'doi', 'paper_title', 'paper_date']
            header = True 

            with open('chagasdb_record_logs.txt', 'w+', encoding='utf-8') as log:
                for index,row in enumerate(reader):
                    # Skip header line
                    if (header): 
                        header = False 
                        continue

                    # Check if entry already exists; if must-filled values are there; if date is set correctly 
                    if overwrite == False: 
                        if Chagas_object.objects.filter(feature_name__iexact = row[0].strip(), feature_type__iexact = row[4].strip(), phenotype1__iexact = row[6].strip(), phenotype2__iexact = row[8].strip(), tissue__iexact = row[10].strip(), organism__iexact = row[18].strip(), pmid__iexact = row[21].strip()).exists():
                            duplicate += 1 # We look if the value in the DB match the one in the row (case insensitive, eventual whitespaces removed)
                            continue              

                    # Create a new object and save it
                    try:
                        entry = Chagas_object()
                        for i in range(len(row)):
                            if row[i].strip() == "" or row[i].strip() == "Unknown":
                                setattr(entry, object_attributes[i], None)
                            else:
                                setattr(entry, object_attributes[i], row[i].strip())
                        entry.save()
                        added += 1
            
                    except Exception as e:
                        log.write("Row N°: "+str(index+1)+" raised an issue: "+str(e)+"\n")
                        failed += 1
                        
                log.write("\n\n\nChagasDB updated:\n\tEntries added: "+str(added)+"\n\tDuplicates found: "+str(duplicate)+"\n\tFailed entries: "+str(failed))
            log.close()
        f.close()
        print("ChagasDB updated:\n\tEntries added:", added, "\n\tDuplicates found:", duplicate, "\n\tFailed entries:", failed, "\n\nCheck log details in chagasdb_record_logs.txt")
    except IndexError:
        print ("Error: File does not appear to be formatted correctly.")
    except Exception as e: print(e)

    return

# Launching the script when called
if __name__ == "__main__":
    # Check if the variable pointing on the database is set up
    DB_FILE = os.getenv('DB_FILE')

    if DB_FILE is None :
        typer.echo("The DB_FILE variable path towards the sql file of ChagasDB is not defined.")
        quit()
    else :
        if os.path.exists(DB_FILE) == False:
            typer.echo("DB_FILE path variable towards the sql file of ChagasDB not correct. Please define it again\n")
            quit()

    print('\n\nRunning may take some time depending on file size, especially if the --overwrite option is not used.')

    typer.run(main)