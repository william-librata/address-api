-- create type
CREATE TYPE geocode_result
AS
(
    address_detail_id VARCHAR,
    latitude NUMERIC(10, 8),
    longitude NUMERIC(11, 8)
);

-- main
CREATE OR REPLACE FUNCTION geocode
(
    house VARCHAR,
    category VARCHAR,
    near VARCHAR,
    street_number VARCHAR,
    road VARCHAR,
    unit VARCHAR,
    level VARCHAR,
    staircase VARCHAR,
    entrance VARCHAR,
    po_box VARCHAR,
    pcode VARCHAR,
    suburb VARCHAR,
    city_district VARCHAR,
    city VARCHAR,
    island VARCHAR,
    state_district VARCHAR,
    state_name VARCHAR,
    country_region VARCHAR,
    country VARCHAR,
    world_region VARCHAR
)
RETURNS TABLE
(
    address_detail_pid VARCHAR,
    latitude NUMERIC(10, 8),
    longitude NUMERIC(11, 8)
)
AS
$function$
DECLARE
    address_detail_pid VARCHAR;
    latitude NUMERIC(10, 8);
    longitude NUMERIC(11, 8);

BEGIN

    SELECT a.address_detail_pid, a.latitude, a.longitude
    INTO address_detail_pid, latitude, longitude
    FROM address a
    WHERE (a.flat_number_combined = unit
            OR a.lot_number_combined = unit
            OR unit IS NULL)
        AND (a.level_number_combined = level
            OR level IS NULL)
        AND a.house_number = street_number
        AND jarowinkler(a.street, road) >= 0.89
        AND (a.locality_name = suburb
            OR suburb IS NULL)
        AND (a.state = state_name
            OR state_name IS NULL)
        AND (a.postcode = pcode
            OR pcode IS NULL)
    ORDER BY jarowinkler(a.street, road) DESC
    LIMIT 1;

    IF address_detail_pid IS NULL THEN
        SELECT a.address_detail_pid, a.latitude, a.longitude
        INTO address_detail_pid, latitude, longitude
        FROM address a
        WHERE (a.flat_number_combined = unit
                OR a.lot_number_combined = unit
                OR unit IS NULL)
            AND (a.level_number_combined = level
                OR level IS NULL)
            AND a.number_first_combined = street_number
            AND jarowinkler(a.street, road) >= 0.89
            AND (a.locality_name = suburb
                OR suburb IS NULL)
            AND (a.state = state_name
                OR state_name IS NULL)
            AND (a.postcode = pcode
                OR pcode IS NULL)
        ORDER BY jarowinkler(a.street, road) DESC
        LIMIT 1;
    END IF;

    IF address_detail_pid IS NULL THEN
        SELECT a.address_detail_pid, a.latitude, a.longitude
        INTO address_detail_pid, latitude, longitude
        FROM address a
        WHERE (a.flat_number_combined = unit
                OR a.lot_number_combined = unit
                OR unit IS NULL)
            AND (a.level_number_combined = level
                OR level IS NULL)
            AND a.number_last_combined = street_number
            AND jarowinkler(a.street, road) >= 0.89
            AND (a.locality_name = suburb
                OR suburb IS NULL)
            AND (a.state = state_name
                OR state_name IS NULL)
            AND (a.postcode = pcode
                OR pcode IS NULL)
        ORDER BY jarowinkler(a.street, road) DESC
        LIMIT 1;
    END IF;

    RETURN QUERY SELECT address_detail_pid, latitude, longitude;

END;
$function$
LANGUAGE plpgsql;

