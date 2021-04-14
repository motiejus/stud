\i wm.sql

--do $$
--begin
--  SET AUTOCOMMIT TO ON;
--end $$ language plpgsql;

-- https://stackoverflow.com/questions/19982373/which-tools-libraries-do-you-use-to-unit-test-your-pl-pgsql
CREATE OR REPLACE FUNCTION assert_equals(expected anyelement, actual anyelement) RETURNS void AS $$
begin
  if expected = actual or (expected is null and actual is null) then
    --do nothing
  else
    raise exception 'Assertion Error. Expected <%> but was <%>', expected, actual;
  end if;
end $$ LANGUAGE plpgsql;

drop function if exists dbg_geomsummary;
create function dbg_geomsummary(geoms geometry[], OUT output text) as $$
  declare i int4;
begin
  output = format('len: %s;', array_length(geoms, 1));
  for i in 1..array_length(geoms, 1) loop
    output = output || format(' %s:%s;', i, st_astext(geoms[i]));
  end loop;
end
$$ language plpgsql;

-- to preview this somewhat conveniently in QGIS:
-- stage || '_' || name || ' gen:' || coalesce(gen, 'Ø') || ' nbend:' || lpad(nbend, 4, '0')
drop table if exists wm_debug;
create table wm_debug(stage text, name text, gen bigint, nbend bigint, way geometry, props jsonb);

drop table if exists wm_figures;
create table wm_figures (name text, way geometry);
-- add fig8.gpkg to postgis:
--   ogr2ogr -update -f PostgreSQL PG:"host=127.0.0.1 user=osm password=osm dbname=osm" fig8.gpkg
-- to "normalize" a new line when it's in `f`:
--   select st_astext(st_snaptogrid(st_transscale(geometry, -19.5, .016, 4000, 4000), 1)) from f;
insert into wm_figures (name, way) values ('fig3',ST_GeomFromText('LINESTRING(0 0,12 0,13 4,20 2,20 0,32 0,33 10,38 16,43 15,44 10,44 0,60 0)'));
insert into wm_figures (name, way) values ('fig3-1',ST_GeomFromText('LINESTRING(0 0,12 0,13 4,20 2,20 0,32 0,33 10,38 16,43 15,44 10,44 0)'));
insert into wm_figures (name, way) values ('fig5',ST_GeomFromText('LINESTRING(0 39,19 52,27 77,26 104,41 115,49 115,65 103,65 75,53 45,63 15,91 0)'));
insert into wm_figures (name, way) values ('fig6',ST_GeomFromText('LINESTRING(84 47,91 59,114 64,122 80,116 92,110 93,106 106,117 118,136 107,135 76,120 45,125 39,141 39,147 32)'));
insert into wm_figures (name, way) values ('fig6-rev',ST_Reverse(ST_Translate((select way from wm_figures where name='fig6'), 60, 0)));
insert into wm_figures (name, way) values ('fig6-combi',
  ST_Union(
      ST_Translate((select way from wm_figures where name='fig6'), 0, 90),
      ST_Translate((select way from wm_figures where name='fig6'), 80, 90)
  )
);
insert into wm_figures (name, way) values('fig8', ST_GeomFromText('LINESTRING(173 12,174 10,180 8,186 8,186 13,191 11,189 6,201 5,203 11,216 16,216 6,222 7,229 3,236 2,239 6,243 8,248 6)'));
insert into wm_figures (name, way) values ('inflection-1',ST_GeomFromText('LINESTRING(110 24,114 20,133 20,145 15,145 0,136 8,123 10,114 10,111 2)'));
insert into wm_figures (name, way) values ('multi-island',ST_GeomFromText('MULTILINESTRING((-15 10,-10 10,-5 11,0 11,5 11,10 10,11 9,13 10,15 9),(-5 11,-2 15,0 16,2 15,5 11))'));

-- TODO: there is a bug and it does not go through `self_crossing` function.
--insert into wm_figures (name, way) values ('selfcrossing-1',ST_GeomFromText('LINESTRING(-27 180,-20 166,-21 142,-18 136,55 136,55 136,71 145,44 165,37 146,22 145,14 164,11 164,3 146,-12 146,-13 176,-18 184)'));

-- Run ST_SimplifyWM in debug mode, so `wm_debug` is populated. That table
-- is used for geometric assertions later in the file.
drop table if exists wm_demo;
create table wm_demo (name text, i bigint, way geometry);

do $$
  declare
    v_state   TEXT;
    v_msg     TEXT;
    v_detail  TEXT;
    v_hint    TEXT;
    v_context TEXT;
begin
insert into wm_demo (name, way) select name, ST_SimplifyWM(way, name) from wm_figures;
exception when others then
    get stacked diagnostics
        v_state   = returned_sqlstate,
        v_msg     = message_text,
        v_detail  = pg_exception_detail,
        v_hint    = pg_exception_hint,
        v_context = pg_exception_context;

    raise notice E'Got exception:
        state  : %
        message: %
        detail : %
        hint   : %
        context: %', v_state, v_msg, v_detail, v_hint, v_context;
end $$ language plpgsql;

-- wm_visuals holds visual aids for the paper.
drop table if exists wm_visuals;
create table wm_visuals (name text, way geometry);
do $$
  declare fig6b1 geometry;
  declare fig6b2 geometry;
begin
  select way from wm_debug where name='fig6' and stage='bbends' and gen=1 into fig6b1 limit 1 offset 0;
  select way from wm_debug where name='fig6' and stage='bbends' and gen=1 into fig6b2 limit 1 offset 2;
  insert into wm_visuals (name, way) values('fig6-baseline', st_makeline(st_startpoint(fig6b2), st_endpoint(fig6b2)));
  insert into wm_visuals (name, way) values('fig6-newline', st_makeline(st_endpoint(fig6b1), st_endpoint(fig6b2)));
end $$ language plpgsql;

do $$
declare
  vbends geometry[];
begin
  select array((select way from wm_debug where name='fig3' and stage='bbends')) into vbends;
  perform assert_equals(5, array_length(vbends, 1));
  perform assert_equals('LINESTRING(0 0,12 0,13 4)', st_astext(vbends[1]));
  perform assert_equals('LINESTRING(12 0,13 4,20 2,20 0)', st_astext(vbends[2]));
  perform assert_equals('LINESTRING(20 2,20 0,32 0,33 10)', st_astext(vbends[3]));
  perform assert_equals('LINESTRING(32 0,33 10,38 16,43 15,44 10,44 0)', st_astext(vbends[4]));
  perform assert_equals(4, array_length(detect_bends((select way from wm_figures where name='fig3-1')), 1));
  select detect_bends((select way from wm_figures where name='fig5')) into vbends;
  perform assert_equals(3, array_length(vbends, 1));
end $$ language plpgsql;

do $$
declare
  vbends geometry[];
  vinflections geometry[];
begin
  select array((select way from wm_debug where name='fig5' and stage='cinflections')) into vinflections;
  perform assert_equals('LINESTRING(0 39,19 52,27 77)', st_astext(vinflections[1]));
  perform assert_equals('LINESTRING(19 52,27 77,26 104,41 115,49 115,65 103,65 75,53 45)', st_astext(vinflections[2]));
  perform assert_equals('LINESTRING(65 75,53 45,63 15,91 0)', st_astext(vinflections[3]));

  -- inflections-1, the example in fix_gentle_inflections docstring
  select array((select way from wm_debug where name='inflection-1' and stage='bbends')) into vbends;
  select array((select way from wm_debug where name='inflection-1' and stage='cinflections')) into vinflections;
  perform assert_equals(vbends[1], vinflections[1]); -- unchanged
  perform assert_equals('LINESTRING(114 20,133 20,145 15,145 0,136 8,123 10,114 10)', st_astext(vinflections[2]));
  perform assert_equals('LINESTRING(123 10,114 10,111 2)', st_astext(vinflections[3]));
end $$ language plpgsql;

do $$
declare
  vcrossings geometry[];
  mutated boolean;
begin
  select (self_crossing(array((select way from wm_debug where stage='cinflections' and name='fig6')))).* into vcrossings, mutated;
  perform assert_equals(true, mutated);
  perform assert_equals(
    'LINESTRING(84 47,91 59,114 64,120 45,125 39,141 39,147 32)',
    (select st_astext(
        st_linemerge(st_union(way))
    ) from (select unnest(vcrossings) way) a)
  );

  select (self_crossing(array((select way from wm_debug where stage='cinflections' and name='fig6-rev')))).* into vcrossings, mutated;
  perform assert_equals(true, mutated);
  perform assert_equals(
    'LINESTRING(84 47,91 59,114 64,120 45,125 39,141 39,147 32)',
    (select st_astext(
        st_translate(st_reverse(st_linemerge(st_union(way))), -60, 0)
    ) from (select unnest(vcrossings) way) a)
  );

  select (self_crossing(array((select way from wm_debug where stage='cinflections' and name='fig6-combi' and gen=1)))).* into vcrossings, mutated;
  perform assert_equals(true, mutated);
  perform assert_equals(
    'MULTILINESTRING((84 137,91 149,114 154,120 135,125 129,141 129,147 122),(164 137,171 149,194 154,200 135,205 129,221 129,227 122))',
    (select st_astext(
        st_linemerge(st_union(way))
    ) from (select unnest(vcrossings) way) a)
  );

end $$ language plpgsql;
