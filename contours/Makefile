#uzupis
#BOUNDS = xmin=582700 ymin=6060750 xmax=584830 ymax=6062750
#krekenava
BOUNDS = xmin=493674 ymin=6146103 xmax=518869 ymax=6171741
XYZ = $(patsubst %.zip,%.xyz,$(wildcard *.zip))
SORT = sort -n -k2 -k1 -t,

.PHONY: all
all: smooth_2_5.gpkg smooth_5.gpkg

smooth_%.gpkg: db/smooth_%
	ogr2ogr $@ "PG:host=127.0.0.1 user=osm dbname=osm" $(basename $@)

db/smooth_%: db/contour_% chaikin.sql
	./managedb -- --echo-all \
		-v ON_ERROR_STOP=1 \
		-v src=$(notdir $(basename $<)) \
		-v tbl=$(notdir $(basename $@)) \
		-f chaikin.sql
	touch $@

db/contour_%: contour_%.gpkg db/.ready
	./managedb -- -c "DROP TABLE IF EXISTS $(basename $<)"
	ogr2ogr -f PostgreSQL "PG:host=127.0.0.1 user=osm dbname=osm" $<
	touch $@

contour_%.gpkg: all.tif
	gdal_contour -nln $(basename $@) -i $(subst _,.,$*) -a z $^ $@

all.tif: all.xyz
	gdal_translate $< $@ \
		-ot Float32 -a_srs EPSG:3346 \
		-co COMPRESS=DEFLATE -co PREDICTOR=2

.INTERMEDIATE: all.xyz
all.xyz: $(XYZ)
	$(SORT) -m $^ > $@

.INTERMEDIATE: $(XYZ)
%.xyz: %.zip
	unzip -qq -c $< $@ | \
		sed -e 's/^ \+//' -e 's/ \+/,/g' | \
		./clip.awk $(addprefix -v ,$(BOUNDS)) | \
		$(SORT) > $@

db/.ready: managedb
	mkdir -p db
	./managedb start
	touch $@
