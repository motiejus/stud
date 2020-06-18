DROP TABLE IF EXISTS :tbl;

CREATE TABLE :tbl (
    fid serial NOT NULL,
    geom geometry(MULTILINESTRING, 3346)
);

INSERT INTO :tbl (geom) (
    SELECT
        ST_ChaikinSmoothing (geom, 5) AS geoms
    FROM
        :src);

