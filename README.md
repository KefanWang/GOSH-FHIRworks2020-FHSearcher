What GOSH-FHIRworks2020-FHSearcher does:

1. Get all patients' names and IDs

2. Generate a spefic patient's pdf document including personal details and all observations. 


How GOSH-FHIRworks2020-FHSearcher does these:

GOSH-FHIRworks2020-FHSearcher is implemented by using python. 

Libraries like request, python-dateutil and FHIR-Parser are used to retrive data and generate document in string form. 

Pdfkit library and wkhtmltopdf tool are used to generate the pdf file.
