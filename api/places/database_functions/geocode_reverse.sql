DROP FUNCTION IF EXISTS geocode
(
    house VARCHAR,
    category VARCHAR,
    near VARCHAR,
    house_number VARCHAR,
    road VARCHAR,
    unit VARCHAR,
    level VARCHAR,
    staircase VARCHAR,
    entrance VARCHAR,
    po_box VARCHAR,
    postcode VARCHAR,
    suburb VARCHAR,
    city_district VARCHAR,
    city VARCHAR,
    island VARCHAR,
    state_district VARCHAR,
    state VARCHAR,
    country_region VARCHAR,
    country VARCHAR,
    world_region VARCHAR
);

DROP TYPE IF EXISTS geocode_result;

