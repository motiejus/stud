DROP TABLE IF EXISTS douglas_:tolerance;

CREATE TABLE douglas_:tolerance (
    fid serial NOT NULL,
    geom geometry(MULTILINESTRING, 3346)
);

INSERT INTO douglas_:tolerance (geom) (
    SELECT
        ST_Simplify (ST_LineMerge (ST_Union (geom)),
            :tolerance) AS geoms
    FROM
        zeimena);

