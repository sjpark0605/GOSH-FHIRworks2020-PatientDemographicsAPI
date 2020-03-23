# GOSH-FHIRworks2020-PatientDemographicsAPI
API that utilizes FHIR records to graph information regarding patients' demographics

## Requirements
- FHIR Records Database: https://github.com/goshdrive/FHIRworks_2020
- FHIR Parser by Ethan: https://github.com/greenfrogs/FHIR-Parser

## Source guide

PatientDemographicsAPI.py
- DemographicsUtility.py - Helper source code that contains functions for graphing and json generation
- PatientDemographicsAPI.py - The API powered by Flask
- templates/Demonstrator.html - HTML for the API Demonstrator
- requirements.txt - version requirements for package

## Deployment Instructions
1. Run the FHIR Records Database by following the deployment guide: https://github.com/goshdrive/FHIRworks_2020/blob/master/README.md 

2. Download the package and install requirements as stated in requirements.txt

3. Execute the PatientDemographicsAPI.py via Python3

- Note: Demonstrator can be accessed at http://localhost:8910/
