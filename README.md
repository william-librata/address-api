Address API
===========

Introduction
------------
REST API for Geocoded National Address File (GNAF) utilizing Django Rest Framework. For more information about the dataset, see 
https://data.gov.au/dataset/ds-dga-19432f89-dc3a-4ef3-b943-5326ef1dbecc/details?q=

Setup
-----
1. Ensure that PostgreSQL is installed. See https://www.postgresql.org/ for more details.
1. Ensure that geocoder is installed. See https://github.com/william-librata/geocoder for more details.  
1. Copy secrets_template.ini in API directory to secrets.ini and fill in the details.
1. To install (currently only for ubuntu):
    ```
    # clone project
    git clone git@github.com:william-librata/address-api.git
    cd address-api
    
    # create and activate virtual env
    python3 -m venv env 
    . env/bin/activate 
    
    # install dependencies
    make
    ```
    
1. To run test:
    ```
    # activate virtual env    
    . env/bin/activate 
   
    # run test
    make test
    ```

1. Once installed, API documentation can be accessed through:
    ```
    <your URL>/swagger-ui/
    ``` 
   
