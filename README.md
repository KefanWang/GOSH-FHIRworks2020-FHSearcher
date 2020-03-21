What GOSH-FHIRworks2020-FHSearcher does:

1. Get all patients' names and IDs

2. Generate a spefic patient's document including personal details and all observations. 


How GOSH-FHIRworks2020-FHSearcher does these:

GOSH-FHIRworks2020-FHSearcher is implemented by python. It uses request, python-dateutil and FHIR-Parser libraries to retrive data and generate document in string. Then it uses pdfkit and wkhtmltopdf to generate the pdf file.
