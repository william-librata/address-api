from django.db import models


class AddressAlias(models.Model):
    address_alias_pid = models.CharField(primary_key=True, max_length=15)
    date_created = models.DateField()
    date_retired = models.DateField(blank=True, null=True)
    principal_pid = models.ForeignKey('AddressDetail', models.DO_NOTHING, db_column='principal_pid', related_name='address_alias_principal_pid')
    alias_pid = models.ForeignKey('AddressDetail', models.DO_NOTHING, db_column='alias_pid', related_name='address_alias_pid')
    alias_type_code = models.ForeignKey('AddressAliasTypeAut', models.DO_NOTHING, db_column='alias_type_code')
    alias_comment = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address_alias'


class AddressAliasTypeAut(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address_alias_type_aut'


class AddressDefaultGeocode(models.Model):
    address_default_geocode_pid = models.CharField(primary_key=True, max_length=15)
    date_created = models.DateField()
    date_retired = models.DateField(blank=True, null=True)
    address_detail_pid = models.ForeignKey('AddressDetail', models.DO_NOTHING, db_column='address_detail_pid')
    geocode_type_code = models.ForeignKey('GeocodeTypeAut', models.DO_NOTHING, db_column='geocode_type_code')
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address_default_geocode'


class AddressDetail(models.Model):
    address_detail_pid = models.CharField(primary_key=True, max_length=15)
    date_created = models.DateField()
    date_last_modified = models.DateField(blank=True, null=True)
    date_retired = models.DateField(blank=True, null=True)
    building_name = models.CharField(max_length=200, blank=True, null=True)
    lot_number_prefix = models.CharField(max_length=2, blank=True, null=True)
    lot_number = models.CharField(max_length=5, blank=True, null=True)
    lot_number_suffix = models.CharField(max_length=2, blank=True, null=True)
    flat_type_code = models.ForeignKey('FlatTypeAut', models.DO_NOTHING, db_column='flat_type_code', blank=True, null=True)
    flat_number_prefix = models.CharField(max_length=2, blank=True, null=True)
    flat_number = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    flat_number_suffix = models.CharField(max_length=2, blank=True, null=True)
    level_type_code = models.ForeignKey('LevelTypeAut', models.DO_NOTHING, db_column='level_type_code', blank=True, null=True)
    level_number_prefix = models.CharField(max_length=2, blank=True, null=True)
    level_number = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    level_number_suffix = models.CharField(max_length=2, blank=True, null=True)
    number_first_prefix = models.CharField(max_length=3, blank=True, null=True)
    number_first = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    number_first_suffix = models.CharField(max_length=2, blank=True, null=True)
    number_last_prefix = models.CharField(max_length=3, blank=True, null=True)
    number_last = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    number_last_suffix = models.CharField(max_length=2, blank=True, null=True)
    street_locality_pid = models.ForeignKey('StreetLocality', models.DO_NOTHING, db_column='street_locality_pid', blank=True, null=True)
    location_description = models.CharField(max_length=45, blank=True, null=True)
    locality_pid = models.ForeignKey('Locality', models.DO_NOTHING, db_column='locality_pid')
    alias_principal = models.CharField(max_length=1, blank=True, null=True)
    postcode = models.CharField(max_length=4, blank=True, null=True)
    private_street = models.CharField(max_length=75, blank=True, null=True)
    legal_parcel_id = models.CharField(max_length=20, blank=True, null=True)
    confidence = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    address_site_pid = models.ForeignKey('AddressSite', models.DO_NOTHING, db_column='address_site_pid')
    level_geocoded_code = models.ForeignKey('GeocodedLevelTypeAut', models.DO_NOTHING, db_column='level_geocoded_code')
    property_pid = models.CharField(max_length=15, blank=True, null=True)
    gnaf_property_pid = models.CharField(max_length=15, blank=True, null=True)
    primary_secondary = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address_detail'


class AddressMeshBlock2011(models.Model):
    address_mesh_block_2011_pid = models.CharField(primary_key=True, max_length=15)
    date_created = models.DateField()
    date_retired = models.DateField(blank=True, null=True)
    address_detail_pid = models.ForeignKey(AddressDetail, models.DO_NOTHING, db_column='address_detail_pid')
    mb_match_code = models.ForeignKey('MbMatchCodeAut', models.DO_NOTHING, db_column='mb_match_code')
    mb_2011_pid = models.ForeignKey('Mb2011', models.DO_NOTHING, db_column='mb_2011_pid')

    class Meta:
        managed = False
        db_table = 'address_mesh_block_2011'


class AddressMeshBlock2016(models.Model):
    address_mesh_block_2016_pid = models.CharField(primary_key=True, max_length=15)
    date_created = models.DateField()
    date_retired = models.DateField(blank=True, null=True)
    address_detail_pid = models.ForeignKey(AddressDetail, models.DO_NOTHING, db_column='address_detail_pid')
    mb_match_code = models.ForeignKey('MbMatchCodeAut', models.DO_NOTHING, db_column='mb_match_code')
    mb_2016_pid = models.ForeignKey('Mb2016', models.DO_NOTHING, db_column='mb_2016_pid')

    class Meta:
        managed = False
        db_table = 'address_mesh_block_2016'


class AddressSite(models.Model):
    address_site_pid = models.CharField(primary_key=True, max_length=15)
    date_created = models.DateField()
    date_retired = models.DateField(blank=True, null=True)
    address_type = models.ForeignKey('AddressTypeAut', models.DO_NOTHING, db_column='address_type', blank=True, null=True)
    address_site_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address_site'


class AddressSiteGeocode(models.Model):
    address_site_geocode_pid = models.CharField(primary_key=True, max_length=15)
    date_created = models.DateField()
    date_retired = models.DateField(blank=True, null=True)
    address_site_pid = models.ForeignKey(AddressSite, models.DO_NOTHING, db_column='address_site_pid', blank=True, null=True)
    geocode_site_name = models.CharField(max_length=200, blank=True, null=True)
    geocode_site_description = models.CharField(max_length=45, blank=True, null=True)
    geocode_type_code = models.ForeignKey('GeocodeTypeAut', models.DO_NOTHING, db_column='geocode_type_code', blank=True, null=True)
    reliability_code = models.ForeignKey('GeocodeReliabilityAut', models.DO_NOTHING, db_column='reliability_code')
    boundary_extent = models.DecimalField(max_digits=7, decimal_places=0, blank=True, null=True)
    planimetric_accuracy = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    elevation = models.DecimalField(max_digits=7, decimal_places=0, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address_site_geocode'


class AddressTypeAut(models.Model):
    code = models.CharField(primary_key=True, max_length=8)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address_type_aut'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FlatTypeAut(models.Model):
    code = models.CharField(primary_key=True, max_length=7)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flat_type_aut'


class GeocodeReliabilityAut(models.Model):
    code = models.DecimalField(primary_key=True, max_digits=1, decimal_places=0)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geocode_reliability_aut'


class GeocodeTypeAut(models.Model):
    code = models.CharField(primary_key=True, max_length=4)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geocode_type_aut'


class GeocodedLevelTypeAut(models.Model):
    code = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geocoded_level_type_aut'


class LevelTypeAut(models.Model):
    code = models.CharField(primary_key=True, max_length=4)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'level_type_aut'


class Locality(models.Model):
    locality_pid = models.CharField(primary_key=True, max_length=15)
    date_created = models.DateField()
    date_retired = models.DateField(blank=True, null=True)
    locality_name = models.CharField(max_length=100)
    primary_postcode = models.CharField(max_length=4, blank=True, null=True)
    locality_class_code = models.ForeignKey('LocalityClassAut', models.DO_NOTHING, db_column='locality_class_code')
    state_pid = models.ForeignKey('State', models.DO_NOTHING, db_column='state_pid')
    gnaf_locality_pid = models.CharField(max_length=15, blank=True, null=True)
    gnaf_reliability_code = models.ForeignKey(GeocodeReliabilityAut, models.DO_NOTHING, db_column='gnaf_reliability_code')

    class Meta:
        managed = False
        db_table = 'locality'


class LocalityAlias(models.Model):
    locality_alias_pid = models.CharField(primary_key=True, max_length=15)
    date_created = models.DateField()
    date_retired = models.DateField(blank=True, null=True)
    locality_pid = models.ForeignKey(Locality, models.DO_NOTHING, db_column='locality_pid')
    name = models.CharField(max_length=100)
    postcode = models.CharField(max_length=4, blank=True, null=True)
    alias_type_code = models.ForeignKey('LocalityAliasTypeAut', models.DO_NOTHING, db_column='alias_type_code')
    state_pid = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'locality_alias'


class LocalityAliasTypeAut(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locality_alias_type_aut'


class LocalityClassAut(models.Model):
    code = models.CharField(primary_key=True, max_length=1)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locality_class_aut'


class LocalityNeighbour(models.Model):
    locality_neighbour_pid = models.CharField(primary_key=True, max_length=15)
    date_created = models.DateField()
    date_retired = models.DateField(blank=True, null=True)
    locality_pid = models.ForeignKey(Locality, models.DO_NOTHING, db_column='locality_pid', related_name='locality_neighbour_locality_pid')
    neighbour_locality_pid = models.ForeignKey(Locality, models.DO_NOTHING, db_column='neighbour_locality_pid', related_name='locality_neighbour_neighbour_locality_pid')

    class Meta:
        managed = False
        db_table = 'locality_neighbour'


class LocalityPoint(models.Model):
    locality_point_pid = models.CharField(primary_key=True, max_length=15)
    date_created = models.DateField()
    date_retired = models.DateField(blank=True, null=True)
    locality_pid = models.ForeignKey(Locality, models.DO_NOTHING, db_column='locality_pid')
    planimetric_accuracy = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locality_point'


class Mb2011(models.Model):
    mb_2011_pid = models.CharField(primary_key=True, max_length=15)
    date_created = models.DateField()
    date_retired = models.DateField(blank=True, null=True)
    mb_2011_code = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'mb_2011'


class Mb2016(models.Model):
    mb_2016_pid = models.CharField(primary_key=True, max_length=15)
    date_created = models.DateField()
    date_retired = models.DateField(blank=True, null=True)
    mb_2016_code = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'mb_2016'


class MbMatchCodeAut(models.Model):
    code = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mb_match_code_aut'


class PrimarySecondary(models.Model):
    primary_secondary_pid = models.CharField(primary_key=True, max_length=15)
    primary_pid = models.ForeignKey(AddressDetail, models.DO_NOTHING, db_column='primary_pid', related_name='primary_secondary_primary_pid')
    secondary_pid = models.ForeignKey(AddressDetail, models.DO_NOTHING, db_column='secondary_pid', related_name='primary_secondary_secondary_pid')
    date_created = models.DateField()
    date_retired = models.DateField(blank=True, null=True)
    ps_join_type_code = models.ForeignKey('PsJoinTypeAut', models.DO_NOTHING, db_column='ps_join_type_code')
    ps_join_comment = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'primary_secondary'


class PsJoinTypeAut(models.Model):
    code = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ps_join_type_aut'


class State(models.Model):
    state_pid = models.CharField(primary_key=True, max_length=15)
    date_created = models.DateField()
    date_retired = models.DateField(blank=True, null=True)
    state_name = models.CharField(max_length=50)
    state_abbreviation = models.CharField(max_length=3)
    created_by = models.CharField(max_length=150, null=True)

    class Meta:
        managed = True
        db_table = 'state'


class StreetClassAut(models.Model):
    code = models.CharField(primary_key=True, max_length=1)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'street_class_aut'


class StreetLocality(models.Model):
    street_locality_pid = models.CharField(primary_key=True, max_length=15)
    date_created = models.DateField()
    date_retired = models.DateField(blank=True, null=True)
    street_class_code = models.ForeignKey(StreetClassAut, models.DO_NOTHING, db_column='street_class_code')
    street_name = models.CharField(max_length=100)
    street_type_code = models.ForeignKey('StreetTypeAut', models.DO_NOTHING, db_column='street_type_code', blank=True, null=True)
    street_suffix_code = models.ForeignKey('StreetSuffixAut', models.DO_NOTHING, db_column='street_suffix_code', blank=True, null=True)
    locality_pid = models.ForeignKey(Locality, models.DO_NOTHING, db_column='locality_pid')
    gnaf_street_pid = models.CharField(max_length=15, blank=True, null=True)
    gnaf_street_confidence = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    gnaf_reliability_code = models.ForeignKey(GeocodeReliabilityAut, models.DO_NOTHING, db_column='gnaf_reliability_code')

    class Meta:
        managed = False
        db_table = 'street_locality'


class StreetLocalityAlias(models.Model):
    street_locality_alias_pid = models.CharField(primary_key=True, max_length=15)
    date_created = models.DateField()
    date_retired = models.DateField(blank=True, null=True)
    street_locality_pid = models.ForeignKey(StreetLocality, models.DO_NOTHING, db_column='street_locality_pid')
    street_name = models.CharField(max_length=100)
    street_type_code = models.ForeignKey('StreetTypeAut', models.DO_NOTHING, db_column='street_type_code', blank=True, null=True)
    street_suffix_code = models.ForeignKey('StreetSuffixAut', models.DO_NOTHING, db_column='street_suffix_code', blank=True, null=True)
    alias_type_code = models.ForeignKey('StreetLocalityAliasTypeAut', models.DO_NOTHING, db_column='alias_type_code')

    class Meta:
        managed = False
        db_table = 'street_locality_alias'


class StreetLocalityAliasTypeAut(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'street_locality_alias_type_aut'


class StreetLocalityPoint(models.Model):
    street_locality_point_pid = models.CharField(primary_key=True, max_length=15)
    date_created = models.DateField()
    date_retired = models.DateField(blank=True, null=True)
    street_locality_pid = models.ForeignKey(StreetLocality, models.DO_NOTHING, db_column='street_locality_pid')
    boundary_extent = models.DecimalField(max_digits=7, decimal_places=0, blank=True, null=True)
    planimetric_accuracy = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'street_locality_point'


class StreetSuffixAut(models.Model):
    code = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'street_suffix_aut'


class StreetTypeAut(models.Model):
    code = models.CharField(primary_key=True, max_length=15)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'street_type_aut'
