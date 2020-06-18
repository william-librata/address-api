from django.db import migrations
from api.settings import BASE_DIR

import os

def create_geocode_database_function(apps, schema_editor):
    file_path = 'places/database_functions/geocode.sql'
    with open(file_path, 'r') as sql_file:
        schema_editor.execute(sql_file.read())


def drop_geocode_database_function(apps, schema_editor):
    file_path = 'places/database_functions/geocode_reverse.sql'
    with open(file_path, 'r') as sql_file:
        schema_editor.execute(sql_file.read())


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_create_database_extension'),
    ]

    operations = [
        migrations.RunPython(create_geocode_database_function, reverse_code=drop_geocode_database_function, atomic=True)
]