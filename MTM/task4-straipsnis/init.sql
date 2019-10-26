CREATE TABLE airports (
    gid SERIAL NOT NULL PRIMARY KEY,
    name TEXT,
    city TEXT,
    country TEXT,
    iata TEXT,
    icao TEXT,
    geom GEOMETRY,
    latitude DOUBLE,
    longitude DOUBLE,
    altitude DOUBLE,
    CONSTRAINT enforce_dims_the_geom CHECK (st_ndims(geom) = 2),
    CONSTRAINT enforce_geotype_geom CHECK (geometrytype(geom) = 'POINT'::text OR geom IS NULL),
    CONSTRAINT enforce_srid_the_geom CHECK (st_srid(the_geom) = 4326)
);
