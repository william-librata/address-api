# Generated by Django 3.0.6 on 2020-06-03 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_detail_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField(blank=True, null=True)),
                ('date_last_modified', models.DateField(blank=True, null=True)),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('building_name', models.CharField(blank=True, max_length=200, null=True)),
                ('lot_number_prefix', models.CharField(blank=True, max_length=2, null=True)),
                ('lot_number', models.CharField(blank=True, max_length=5, null=True)),
                ('lot_number_suffix', models.CharField(blank=True, max_length=2, null=True)),
                ('lot_number_combined', models.TextField(blank=True, null=True)),
                ('flat_type_code', models.CharField(blank=True, max_length=7, null=True)),
                ('flat_number_prefix', models.CharField(blank=True, max_length=2, null=True)),
                ('flat_number', models.DecimalField(blank=True, decimal_places=0, max_digits=5, null=True)),
                ('flat_number_suffix', models.CharField(blank=True, max_length=2, null=True)),
                ('flat_number_combined', models.TextField(blank=True, null=True)),
                ('level_type_code', models.CharField(blank=True, max_length=4, null=True)),
                ('level_number_prefix', models.CharField(blank=True, max_length=2, null=True)),
                ('level_number', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('level_number_suffix', models.CharField(blank=True, max_length=2, null=True)),
                ('level_number_combined', models.TextField(blank=True, null=True)),
                ('number_first_prefix', models.CharField(blank=True, max_length=3, null=True)),
                ('number_first', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('number_first_suffix', models.CharField(blank=True, max_length=2, null=True)),
                ('number_first_combined', models.TextField(blank=True, null=True)),
                ('number_last_prefix', models.CharField(blank=True, max_length=3, null=True)),
                ('number_last', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('number_last_suffix', models.CharField(blank=True, max_length=2, null=True)),
                ('number_last_combined', models.TextField(blank=True, null=True)),
                ('house_number', models.TextField(blank=True, null=True)),
                ('street_locality_pid', models.CharField(blank=True, max_length=15, null=True)),
                ('street_name', models.CharField(blank=True, max_length=100, null=True)),
                ('street_type', models.CharField(blank=True, max_length=50, null=True)),
                ('street_suffix_code', models.CharField(blank=True, max_length=15, null=True)),
                ('street_suffix_name', models.CharField(blank=True, max_length=50, null=True)),
                ('street', models.TextField(blank=True, null=True)),
                ('locality_pid', models.CharField(blank=True, max_length=15, null=True)),
                ('locality_name', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=3, null=True)),
                ('alias_principal', models.CharField(blank=True, max_length=1, null=True)),
                ('postcode', models.CharField(blank=True, max_length=4, null=True)),
                ('confidence', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('address_site_pid', models.CharField(blank=True, max_length=15, null=True)),
                ('address_type_name', models.CharField(blank=True, max_length=50, null=True)),
                ('address_site_name', models.CharField(blank=True, max_length=200, null=True)),
                ('level_geocoded_code', models.DecimalField(blank=True, decimal_places=0, max_digits=2, null=True)),
                ('primary_secondary', models.CharField(blank=True, max_length=1, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True)),
            ],
            options={
                'db_table': 'address',
                'managed': True,
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
                'managed': True,
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
                'managed': True,
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
                'managed': True,
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
                'managed': True,
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
                'managed': True,
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
                'managed': True,
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
                'managed': True,
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
                'managed': True,
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
                'managed': True,
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
                ('gnaf_reliability_code', models.ForeignKey(db_column='gnaf_reliability_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='geocodereliabilityaut', to='places.GeocodeReliabilityAut')),
            ],
            options={
                'db_table': 'locality',
                'managed': True,
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
                'managed': True,
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
                'managed': True,
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
                'managed': True,
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
                'managed': True,
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
                'managed': True,
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
                'managed': True,
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
            ],
            options={
                'db_table': 'state',
                'managed': True,
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
                'managed': True,
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
                ('gnaf_reliability_code', models.ForeignKey(db_column='gnaf_reliability_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.GeocodeReliabilityAut')),
                ('locality_pid', models.ForeignKey(db_column='locality_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.Locality')),
                ('street_class_code', models.ForeignKey(db_column='street_class_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.StreetClassAut')),
            ],
            options={
                'db_table': 'street_locality',
                'managed': True,
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
                'managed': True,
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
                'managed': True,
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
                'managed': True,
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
                ('street_locality_pid', models.ForeignKey(db_column='street_locality_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.StreetLocality')),
            ],
            options={
                'db_table': 'street_locality_point',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='StreetLocalityAlias',
            fields=[
                ('street_locality_alias_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('street_name', models.CharField(max_length=100)),
                ('alias_type_code', models.ForeignKey(db_column='alias_type_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.StreetLocalityAliasTypeAut')),
                ('street_locality_pid', models.ForeignKey(db_column='street_locality_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.StreetLocality')),
                ('street_suffix_code', models.ForeignKey(blank=True, db_column='street_suffix_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.StreetSuffixAut')),
                ('street_type_code', models.ForeignKey(blank=True, db_column='street_type_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.StreetTypeAut')),
            ],
            options={
                'db_table': 'street_locality_alias',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='streetlocality',
            name='street_suffix_code',
            field=models.ForeignKey(blank=True, db_column='street_suffix_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.StreetSuffixAut'),
        ),
        migrations.AddField(
            model_name='streetlocality',
            name='street_type_code',
            field=models.ForeignKey(blank=True, db_column='street_type_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.StreetTypeAut'),
        ),
        migrations.CreateModel(
            name='PrimarySecondary',
            fields=[
                ('primary_secondary_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('ps_join_comment', models.CharField(blank=True, max_length=500, null=True)),
                ('primary_pid', models.ForeignKey(db_column='primary_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='primary_secondary_primary_pid', to='places.AddressDetail')),
                ('ps_join_type_code', models.ForeignKey(db_column='ps_join_type_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.PsJoinTypeAut')),
                ('secondary_pid', models.ForeignKey(db_column='secondary_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='primary_secondary_secondary_pid', to='places.AddressDetail')),
            ],
            options={
                'db_table': 'primary_secondary',
                'managed': True,
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
                ('locality_pid', models.ForeignKey(db_column='locality_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.Locality')),
            ],
            options={
                'db_table': 'locality_point',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='LocalityNeighbour',
            fields=[
                ('locality_neighbour_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('locality_pid', models.ForeignKey(db_column='locality_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='locality_neighbour_locality_pid', to='places.Locality')),
                ('neighbour_locality_pid', models.ForeignKey(db_column='neighbour_locality_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='locality_neighbour_neighbour_locality_pid', to='places.Locality')),
            ],
            options={
                'db_table': 'locality_neighbour',
                'managed': True,
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
                ('alias_type_code', models.ForeignKey(db_column='alias_type_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.LocalityAliasTypeAut')),
                ('locality_pid', models.ForeignKey(db_column='locality_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.Locality')),
            ],
            options={
                'db_table': 'locality_alias',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='locality',
            name='locality_class_code',
            field=models.ForeignKey(db_column='locality_class_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='localityclassaut', to='places.LocalityClassAut'),
        ),
        migrations.AddField(
            model_name='locality',
            name='state_pid',
            field=models.ForeignKey(db_column='state_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='state', to='places.State'),
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
                ('address_site_pid', models.ForeignKey(blank=True, db_column='address_site_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.AddressSite')),
                ('geocode_type_code', models.ForeignKey(blank=True, db_column='geocode_type_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.GeocodeTypeAut')),
                ('reliability_code', models.ForeignKey(db_column='reliability_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.GeocodeReliabilityAut')),
            ],
            options={
                'db_table': 'address_site_geocode',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='addresssite',
            name='address_type',
            field=models.ForeignKey(blank=True, db_column='address_type', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.AddressTypeAut'),
        ),
        migrations.CreateModel(
            name='AddressMeshBlock2016',
            fields=[
                ('address_mesh_block_2016_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('address_detail_pid', models.ForeignKey(db_column='address_detail_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.AddressDetail')),
                ('mb_2016_pid', models.ForeignKey(db_column='mb_2016_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.Mb2016')),
                ('mb_match_code', models.ForeignKey(db_column='mb_match_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.MbMatchCodeAut')),
            ],
            options={
                'db_table': 'address_mesh_block_2016',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AddressMeshBlock2011',
            fields=[
                ('address_mesh_block_2011_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('address_detail_pid', models.ForeignKey(db_column='address_detail_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.AddressDetail')),
                ('mb_2011_pid', models.ForeignKey(db_column='mb_2011_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.Mb2011')),
                ('mb_match_code', models.ForeignKey(db_column='mb_match_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.MbMatchCodeAut')),
            ],
            options={
                'db_table': 'address_mesh_block_2011',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='addressdetail',
            name='address_site_pid',
            field=models.ForeignKey(db_column='address_site_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.AddressSite'),
        ),
        migrations.AddField(
            model_name='addressdetail',
            name='flat_type_code',
            field=models.ForeignKey(blank=True, db_column='flat_type_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.FlatTypeAut'),
        ),
        migrations.AddField(
            model_name='addressdetail',
            name='level_geocoded_code',
            field=models.ForeignKey(db_column='level_geocoded_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.GeocodedLevelTypeAut'),
        ),
        migrations.AddField(
            model_name='addressdetail',
            name='level_type_code',
            field=models.ForeignKey(blank=True, db_column='level_type_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.LevelTypeAut'),
        ),
        migrations.AddField(
            model_name='addressdetail',
            name='locality_pid',
            field=models.ForeignKey(db_column='locality_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.Locality'),
        ),
        migrations.AddField(
            model_name='addressdetail',
            name='street_locality_pid',
            field=models.ForeignKey(blank=True, db_column='street_locality_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.StreetLocality'),
        ),
        migrations.CreateModel(
            name='AddressDefaultGeocode',
            fields=[
                ('address_default_geocode_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('address_detail_pid', models.ForeignKey(db_column='address_detail_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.AddressDetail')),
                ('geocode_type_code', models.ForeignKey(db_column='geocode_type_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.GeocodeTypeAut')),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'address_default_geocode',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AddressAlias',
            fields=[
                ('address_alias_pid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('date_created', models.DateField()),
                ('date_retired', models.DateField(blank=True, null=True)),
                ('alias_comment', models.CharField(blank=True, max_length=200, null=True)),
                ('alias_pid', models.ForeignKey(db_column='alias_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='address_alias_pid', to='places.AddressDetail')),
                ('alias_type_code', models.ForeignKey(db_column='alias_type_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.AddressAliasTypeAut')),
                ('principal_pid', models.ForeignKey(db_column='principal_pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='address_alias_principal_pid', to='places.AddressDetail')),
            ],
            options={
                'db_table': 'address_alias',
                'managed': True,
            },
        ),
    ]
