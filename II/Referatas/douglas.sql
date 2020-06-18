DROP TABLE IF EXISTS :tbl;

CREATE TABLE :tbl (
    fid serial NOT NULL,
    geom geometry(MULTILINESTRING, 3346)
);

INSERT INTO :tbl (geom) (
    SELECT
        ST_Multi (ST_Simplify (ST_LineMerge (ST_Union (geom)),
                :param1)) AS geoms
    FROM
        :src);

