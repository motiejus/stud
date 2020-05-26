DROP TABLE IF EXISTS :tbl;

CREATE TABLE :tbl (
    fid serial NOT NULL,
    geom geometry(MULTILINESTRING, 3346)
);

INSERT INTO :tbl (geom) (
    SELECT
        ST_SimplifyVW (ST_LineMerge (ST_Union (geom)),
            :tolerance * :tolerance) AS geoms
    FROM
        :src);

