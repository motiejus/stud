DROP TABLE IF EXISTS :tbl;

CREATE TABLE :tbl (
    fid serial NOT NULL,
    z DOUBLE PRECISION,
    geom geometry(MULTILINESTRING, 3346)
);

INSERT INTO :tbl (
    SELECT
        fid,
        z,
        ST_Multi(
            ST_ChaikinSmoothing (
                ST_SimplifyVW(geom, 50),
                5
            )
        ) AS geoms
    FROM
        :src);
