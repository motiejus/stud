CROSSING=622916 6109267 626066 6111487 # xmin ymin xmax ymax
ZEIMENA_TOLERANCES = 128 256 512 1024 2048 4096
SINEWAVE_TOLERANCES = 1 20 30 40
CROSSING_TOLERANCES = 64 128 256
GEN1 = $(addsuffix .pdf, \
		  $(addprefix sinewave-douglas-,$(SINEWAVE_TOLERANCES)) \
		  $(addprefix sinewave-visvalingam-,$(SINEWAVE_TOLERANCES)) \
		  $(addprefix zeimena-douglas-,$(ZEIMENA_TOLERANCES)) \
		  $(addprefix zeimena-visvalingam-,$(ZEIMENA_TOLERANCES)))

GEN2 = $(addsuffix .pdf, \
		   $(addprefix crossing-zeimena-douglas-,$(CROSSING_TOLERANCES)) \
		   $(addprefix crossing-zeimena-visvalingam-,$(CROSSING_TOLERANCES)))

mj-referatas.pdf: mj-referatas.tex version.tex bib.bib zeimena.pdf \
	sinewave.pdf crossing.pdf $(GEN1) $(GEN2)
	latexmk -g -pdf $<

define algo2img
db/.faux_$(1)-$(2)-%: $(2).sql db/.faux_ready
	./managedb -- --echo-all -v ON_ERROR_STOP=1 -v src=$(1) -v tolerance=$$* -v tbl=$(1)_$(2)_$$* -f $(2).sql
	touch $$@
$(1)-$(2)-%.pdf: layer2img.py db/.faux_$(1)-$(2)-%
	./layer2img.py --group2-table=$(1)_$(2)_$$* --size=$(3) --outfile $$@
endef

define algo2overlay
crossing-$(1)-$(2)-%.pdf: layer2img.py db/.faux_$(1)-$(2)-%
	./layer2img.py $(3) --group1-table=$(1) --group2-table=$(1)_$(2)_$$* --outfile $$@
endef

define gpkg2pdf
$(1): $(2) ./layer2img.py
	./layer2img.py $(3) --group1-infile=$$< --outfile $(1)
endef

$(eval $(call algo2img,sinewave,douglas,60x24))
$(eval $(call algo2img,sinewave,visvalingam,60x24))
$(eval $(call algo2img,zeimena,douglas,210x297))
$(eval $(call algo2img,zeimena,visvalingam,210x297))
$(eval $(call gpkg2pdf,sinewave.pdf,sinewave.gpkg,,--size=60x24))
$(eval $(call gpkg2pdf,zeimena.pdf,zeimena.gpkg rectangle.gpkg,--size=67x95 --group2-infile rectangle.gpkg))
$(eval $(call gpkg2pdf,crossing.pdf,zeimena.gpkg,--size=105x74 --clip $(CROSSING)))
$(eval $(call algo2overlay,zeimena,douglas,--size 297x210 --clip $(CROSSING)))
$(eval $(call algo2overlay,zeimena,visvalingam,--size 297x210 --clip $(CROSSING)))

sinewave.gpkg: fig2layer.py
	./fig2layer.py -o $@ sine

rectangle.gpkg: fig2layer.py
	./fig2layer.py -o $@ rect --bounds $(CROSSING)

db/.faux_ready: zeimena.gpkg sinewave.gpkg managedb
	-./managedb stop; rm -fr db
	./managedb init
	ogr2ogr -f PostgreSQL "PG:host=127.0.0.1 user=osm dbname=osm" zeimena.gpkg
	ogr2ogr -f PostgreSQL "PG:host=127.0.0.1 user=osm dbname=osm" sinewave.gpkg
	touch $@

REF = $(shell git describe --tags)
DIRTY = $(shell git status --porcelain | awk '{print"-dirty";exit}')
GIT_DIR = $(shell git rev-parse --show-toplevel)/.git
version.tex: $(shell git ls-files .) $(GIT_DIR)
	( \
		date '+\gdef\GeneratedAt{%F %T %Z}%'; \
		printf '\gdef\VCDescribe{%s%s}%%\n' $(REF) $(DIRTY); \
	) > $@
