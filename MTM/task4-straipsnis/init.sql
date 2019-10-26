-- schema
CREATE TABLE airports (
    gid SERIAL NOT NULL PRIMARY KEY,
    name TEXT,
    city TEXT,
    country TEXT,
    iata TEXT,
    icao TEXT,
    geom GEOMETRY,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    altitude DOUBLE PRECISION,
    timezone TEXT,
    dst TEXT,
    tz TEXT,
    type TEXT,
    source TEXT,
    CONSTRAINT enforce_dims_geom CHECK (st_ndims(geom) = 2),
    CONSTRAINT enforce_geotype_geom CHECK (geometrytype(geom) = 'POINT'::text OR geom IS NULL),
    CONSTRAINT enforce_srid_geom CHECK (st_srid(geom) = 4326)
);

-- import data from airports.dat
\copy airports(gid, name, city, country, iata, icao, latitude, longitude, altitude, timezone, dst, tz, type, source) FROM 'airports.dat' DELIMITERS ',' CSV;

-- put lat/lon to the real GIS "geom" field
UPDATE airports
SET geom = ST_SetSRID(ST_Point(longitude, latitude),4326);
