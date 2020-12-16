include config.mk

OUTSIZE = $(shell awk $(addprefix -v ,$(BOUNDS)) 'BEGIN{print ymax-ymin" "xmax-xmin}' /dev/null)
XYZ = $(patsubst %.zip,%.xyz,$(wildcard 6*.zip))
SORT = sort -n -k2 -k1 -t,

.PHONY: all
all: smooth_2_5.gpkg smooth_5.gpkg

smooth_%.gpkg: db/smooth_%
	ogr2ogr $@ "PG:host=127.0.0.1 user=osm dbname=osm password=osm" $(basename $@)

db/smooth_%: db/contour_% chaikin.sql
	./managedb -- --echo-all \
		-v ON_ERROR_STOP=1 \
		-v src=$(notdir $(basename $<)) \
		-v tbl=$(notdir $(basename $@)) \
		-f chaikin.sql
	touch $@

db/contour_%: contour_%.gpkg db/.ready
	./managedb -- -c "DROP TABLE IF EXISTS $(basename $<)"
	ogr2ogr -f PostgreSQL "PG:host=127.0.0.1 user=osm dbname=osm password=osm" $<
	touch $@

contour_%.gpkg: all.tif
	gdal_contour -nln $(basename $@) -i $(subst _,.,$*) -a z $^ $@

ifeq ($(VARIANT),2009)
all.tif: all.vrt all.xyz
	gdal_grid $< $@ \
		-a nearest \
		-ot Float32 -co COMPRESS=DEFLATE -co PREDICTOR=2 \
		-outsize $(OUTSIZE)
else
ifeq ($(VARIANT),2017)
all.tif: all.vrt all.xyz
	gdal_translate $< $@ \
		-ot Float32 -a_srs EPSG:3346 \
		-co COMPRESS=DEFLATE -co PREDICTOR=2
else
$(error VARIANT must be 2009 or 2017)
endif
endif

.INTERMEDIATE: all.xyz
all.xyz: $(XYZ)
	$(SORT) -m $^ > $@

.INTERMEDIATE: $(XYZ)
%.xyz: %.zip
	unzip -qq -c $< $@ | \
		./clip-2009.awk $(addprefix -v ,$(BOUNDS)) | \
		$(SORT) > $@

db/.ready: managedb
	mkdir -p db
	./managedb start
	touch $@
