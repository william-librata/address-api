# Generated by Django 3.0.6 on 2020-05-13 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressAlias',
            fields=[
                ('address_alias_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('alias_comment', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'address_alias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AddressAliasTypeAut',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'address_alias_type_aut',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AddressDefaultGeocode',
            fields=[
                ('address_default_geocode_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'address_default_geocode',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AddressDetail',
            fields=[
                ('address_detail_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_last_modified', models.DateField(blank=True, null=True)),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('building_name', models.CharField(blank=True, max_length=200, null=True)),
                ('lot_number_prefix', models.CharField(blank=True, max_length=2, null=True)),
                ('lot_number', models.CharField(blank=True, max_length=5, null=True)),
                ('lot_number_suffix', models.CharField(blank=True, max_length=2, null=True)),
                ('flat_number_prefix', models.CharField(blank=True, max_length=2, null=True)),
                ('flat_number', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
                ('flat_number_suffix', models.CharField(blank=True, max_length=2, null=True)),
                ('level_number_prefix', models.CharField(blank=True, max_length=2, null=True)),
                ('level_number', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('level_number_suffix', models.CharField(blank=True, max_length=2, null=True)),
                ('number_first_prefix', models.CharField(blank=True, max_length=3, null=True)),
                ('number_first', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('number_first_suffix', models.CharField(blank=True, max_length=2, null=True)),
                ('number_last_prefix', models.CharField(blank=True, max_length=3, null=True)),
                ('number_last', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('number_last_suffix', models.CharField(blank=True, max_length=2, null=True)),
                ('location_description', models.CharField(blank=True, max_length=45, null=True)),
                ('alias_principal', models.CharField(blank=True, max_length=1, null=True)),
                ('postcode', models.CharField(blank=True, max_length=4, null=True)),
                ('private_street', models.CharField(blank=True, max_length=75, null=True)),
                ('legal_parcel_id', models.CharField(blank=True, max_length=20, null=True)),
                ('confidence', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('property_pid', models.CharField(blank=True, max_length=15, null=True)),
                ('gnaf_property_pid', models.CharField(blank=True, max_length=15, null=True)),
                ('primary_secondary', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'address_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AddressMeshBlock2011',
            fields=[
                ('address_mesh_block_2011_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'address_mesh_block_2011',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AddressMeshBlock2016',
            fields=[
                ('address_mesh_block_2016_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'address_mesh_block_2016',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AddressSite',
            fields=[
                ('address_site_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('address_site_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'address_site',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AddressSiteGeocode',
            fields=[
                ('address_site_geocode_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('geocode_site_name', models.CharField(blank=True, max_length=200, null=True)),
                ('geocode_site_description', models.CharField(blank=True, max_length=45, null=True)),
                ('boundary_extent', models.DecimalField(blank=True, decimal_places=0, max_digits=7, null=True)),
                ('planimetric_accuracy', models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True)),
                ('elevation', models.DecimalField(blank=True, decimal_places=0, max_digits=7, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'address_site_geocode',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AddressTypeAut',
            fields=[
                ('code', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'address_type_aut',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FlatTypeAut',
            fields=[
                ('code', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'flat_type_aut',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GeocodedLevelTypeAut',
            fields=[
                ('code', models.DecimalField(decimal_places=0, max_digits=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=70, null=True)),
            ],
            options={
                'db_table': 'geocoded_level_type_aut',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GeocodeReliabilityAut',
            fields=[
                ('code', models.DecimalField(decimal_places=0, max_digits=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'geocode_reliability_aut',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GeocodeTypeAut',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'geocode_type_aut',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LevelTypeAut',
            fields=[
                ('code', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'level_type_aut',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('locality_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('locality_name', models.CharField(max_length=100)),
                ('primary_postcode', models.CharField(blank=True, max_length=4, null=True)),
                ('gnaf_locality_pid', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'locality',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LocalityAlias',
            fields=[
                ('locality_alias_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('postcode', models.CharField(blank=True, max_length=4, null=True)),
                ('state_pid', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'locality_alias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LocalityAliasTypeAut',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'locality_alias_type_aut',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LocalityClassAut',
            fields=[
                ('code', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'locality_class_aut',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LocalityNeighbour',
            fields=[
                ('locality_neighbour_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'locality_neighbour',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LocalityPoint',
            fields=[
                ('locality_point_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('planimetric_accuracy', models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'locality_point',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mb2011',
            fields=[
                ('mb_2011_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('mb_2011_code', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'mb_2011',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mb2016',
            fields=[
                ('mb_2016_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('mb_2016_code', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'mb_2016',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MbMatchCodeAut',
            fields=[
                ('code', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'db_table': 'mb_match_code_aut',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PrimarySecondary',
            fields=[
                ('primary_secondary_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('ps_join_comment', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'primary_secondary',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PsJoinTypeAut',
            fields=[
                ('code', models.DecimalField(decimal_places=0, max_digits=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'ps_join_type_aut',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('state_name', models.CharField(max_length=50)),
                ('state_abbreviation', models.CharField(max_length=3)),
                ('created_by', models.CharField(max_length=150, null=True)),
            ],
            options={
                'db_table': 'state',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StreetClassAut',
            fields=[
                ('code', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'street_class_aut',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StreetLocality',
            fields=[
                ('street_locality_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('street_name', models.CharField(max_length=100)),
                ('gnaf_street_pid', models.CharField(blank=True, max_length=15, null=True)),
                ('gnaf_street_confidence', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
            ],
            options={
                'db_table': 'street_locality',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StreetLocalityAlias',
            fields=[
                ('street_locality_alias_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('street_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'street_locality_alias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StreetLocalityAliasTypeAut',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'street_locality_alias_type_aut',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StreetLocalityPoint',
            fields=[
                ('street_locality_point_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('boundary_extent', models.DecimalField(blank=True, decimal_places=0, max_digits=7, null=True)),
                ('planimetric_accuracy', models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'street_locality_point',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StreetSuffixAut',
            fields=[
                ('code', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'street_suffix_aut',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StreetTypeAut',
            fields=[
                ('code', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'street_type_aut',
                'managed': False,
            },
        ),
    ]
