from django.db import migrations


def create_pg_similarity_extension(apps, schema_editor):
    schema_editor.execute("CREATE EXTENSION pg_similarity;")


def drop_pg_similarity_extension(apps, schema_editor):
    schema_editor.execute("DROP EXTENSION IF EXISTS pg_similarity;")


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_pg_similarity_extension, reverse_code=drop_pg_similarity_extension, atomic=True)
]