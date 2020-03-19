from fhir_parser import FHIR
import pdfkit

fhir = FHIR()
def showOptions():
    print("Please select what you want to do:\n")
    print("1. Generate documents\n")
    print("2. Return to last page\n")
def getPatient(patient_id):
    return fhir.get_patient(patient_id)
def getObservation(patient_id):
    return fhir.get_patient_observations(patient_id)
def patientDocument():
    result = "Patient Name: " + patient.full_name() + "<br>"
    result += "<br>"
    result += "Id: " + patient.uuid + "<br>"
    result += "<br>"
    result += "Age: " + str(patient.age()) + "<br>"
    result += "<br>"
    result += "Gender: " + patient.gender + "<br>"  
    result += "<br>"
    result += "Addresses: <br>"
    for x in patient.addresses:
        result += x.full_address + "<br>"
    result += "<br>"
    result += "Birthdate: " + str(patient.birth_date) + "<br>" 
    result += "<br>"
    result += "communications: " + str(patient.communications) + "<br>"
    result += "<br>"
    #for x in patient.communications:
    #    result+= x + " "
    #result += "<br>"
    result += "Marital status: " + str(patient.marital_status) + "<br>" 
    result += "<br>"
    result += "Multiple birth: " + str(patient.multiple_birth) + "<br>" 
    result += "<br>"
    result += "Telecoms: <br>" 
    for x in patient.telecoms:
        result += str(x) + '<br>'
    result += "<br>"
    result += "Identifiers:<br> "
    for x in patient.identifiers:
        result += str(x) + '<br>'
    result += "<br>"
    result += "Extensions:<br>"
    for x in patient.extensions:
        result += str(x) + '<br> '
    result += "<br>"
    return result
def observationDocument():
    result = ""
    for x in observaions:
        result += "---------------------------------------------<br>"
        result += "Observation id: " + x.uuid + "<br><br>"
        result += "Issued datetime: " + str(x.issued_datetime) + "<br><br>"
        result += "Effective datetime: " + str(x.effective_datetime) + "<br><br>"
        result += "Type: " + x.type + "<br><br>"
        result += "Status: " + x.status + "<br><br>"
        result += "Encounter id: " + x.encounter_uuid + "<br><br>"
        result += "Observation components:<br><br>"
        for y in x.components:
            result += "code: " + y.code +"<br><br>"
            result += "display:" + y.display + "<br><br>"
            result += "system:" +y.system +"<br><br>"
            result += "unit:" + str(y.unit) + "<br><br>"
            result += "value:" + str(y.value) + "<br><br>"
    return result
def generateDocuments():
    pdfkit.from_string(patientDocument()+observationDocument(),"document.pdf") 

print("Welcome to FHSearcher!\tType \"help\" to get all patients.\t Press Ctrl+C to shut down.\n")
try:
    while(1==1):
        try:
            patient = None
            observation = None
            patient_id = input("Please input one patient id: ")
            if(patient_id == 'help'):
                print("Generating data...")
                tmp = fhir.get_all_patients()
                for x in tmp:
                    print(str(x.name) + "\t" + str(x.uuid) + "\n")
                continue
            else:
                patient = getPatient(patient_id)
                observaions = getObservation(patient_id)
        except ConnectionError:
            print("Patient does not exist!")
            continue
        else:
            while(1 == 1):
                print("Patient Name:\t", patient.name,"\n")
                showOptions()
                choice = input()
                if(choice == "1"):
                    generateDocuments()
                    continue
                elif(choice == '2'):
                    break
                else:
                    print("Choice does not exist!\n")
                    continue
            continue
except KeyboardInterrupt:
    exit()

