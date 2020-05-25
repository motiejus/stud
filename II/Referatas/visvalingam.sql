DROP TABLE IF EXISTS visvalingam_:tolerance;

CREATE TABLE visvalingam_:tolerance (
    fid serial NOT NULL,
    geom geometry(MULTILINESTRING, 3346)
);

INSERT INTO visvalingam_:tolerance (geom) (
    SELECT
        ST_SimplifyVW (ST_LineMerge (ST_Union (geom)),
            :tolerance * :tolerance) AS geoms
    FROM
        zeimena);

