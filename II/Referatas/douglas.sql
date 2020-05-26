DROP TABLE IF EXISTS :tbl;

CREATE TABLE :tbl (
    fid serial NOT NULL,
    geom geometry(MULTILINESTRING, 3346)
);

INSERT INTO :tbl (geom) (
    SELECT
        ST_Simplify (ST_LineMerge (ST_Union (geom)),
            :tolerance) AS geoms
    FROM
        :src);

