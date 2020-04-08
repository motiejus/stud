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
    CONSTRAINT enforce_dims_geom CHECK (st_ndims(geom) = 3),
    CONSTRAINT enforce_geotype_geom CHECK (geometrytype(geom) = 'POINT'::text OR geom IS NULL),
    CONSTRAINT enforce_srid_geom CHECK (st_srid(geom) = 4326)
);
-- create index for faster spatial lookups
CREATE INDEX idx_geom ON airports USING GIN (geom);

-- import data from airports.dat
\copy airports(gid, name, city, country, iata, icao, latitude, longitude, altitude, timezone, dst, tz, type, source) FROM 'airports.dat' DELIMITERS ',' CSV;

-- put lat/lon/altitude to the "real" geom field
UPDATE airports
SET geom = ST_SetSRID(ST_MakePoint(longitude, latitude, altitude * 0.3048),4326);

ALTER TABLE airports DROP COLUMN latitude;
ALTER TABLE airports DROP COLUMN longitude;
ALTER TABLE airports DROP COLUMN altitude;
ALTER TABLE airports DROP COLUMN type;
ALTER TABLE airports DROP COLUMN source;
