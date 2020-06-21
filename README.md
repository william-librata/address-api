Places API
===========

Introduction
------------
REST API for Geocoded National Address File (GNAF) utilizing Django Rest Framework. For more information about the dataset, see 
https://data.gov.au/dataset/ds-dga-19432f89-dc3a-4ef3-b943-5326ef1dbecc/details?q=

Setup
-----
1. Ensure that PostgreSQL is installed. See https://www.postgresql.org/ for more details.
1. Copy secrets_template.ini in API directory to secrets.ini and fill in the details.
1. To install (currently only for ubuntu):
    ```
    # clone project
    git clone git@github.com:william-librata/places-api.git
    cd places-api
    
    # create and activate virtual env
    python3 -m venv env 
    . env/bin/activate 
    
    # install dependencies
    make
   
    # setup database schema
    make database
    ```
    
1. To run test:
    ```
    # activate virtual env    
    . env/bin/activate 
   
    # run test
    make test
    ```
   
1. To test functionality:
    ```
    # activate virtual env
    . env/bin/activate
   
    # run django dev server
    cd api
    ./manage.py runserver
    ```
1. Open your browser and go to:
    ```
    http://127.0.0.1:8000/
    ```

1. API documentation can be accessed through:
    ```
    <your URL>/swagger-ui/
    ``` 
  
1. To create ERD:
    1. Install Java
    1. Run:
    ```
	java -jar bin/schemaSpy_5.0.0.jar -t pgsql -db <database name> -host <host name> -s <schema name> -u <user name> -p <password> -o <output path> -dp bin/postgresql-42.2.2.jar
    ``` 
