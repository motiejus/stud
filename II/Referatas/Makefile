CROSSING=622916.858 6109272.561 626066.858 6111492.561 # xmin ymin xmax ymax
ZEIMENA_TOLERANCES = 100 125 250 500 1000 2000 4000
SINEWAVE_TOLERANCES = 1 2 3 4
GEN = $(addsuffix .pdf, \
		  $(addprefix sinewave-douglas-,$(SINEWAVE_TOLERANCES)) \
		  $(addprefix sinewave-visvalingam-,$(SINEWAVE_TOLERANCES)) \
		  $(addprefix zeimena-douglas-,$(ZEIMENA_TOLERANCES)) \
		  $(addprefix zeimena-visvalingam-,$(ZEIMENA_TOLERANCES)))

mj-referatas.pdf: mj-referatas.tex version.tex bib.bib zeimena.pdf \
	sinewave.pdf crossing.pdf $(GEN)
	latexmk -g -pdf $<

define algo2img
db/.faux_$(1)-$(2)-%: $(2).sql db/.faux_ready
	./managedb -- --echo-all -v ON_ERROR_STOP=1 -v src=$(1) -v tolerance=$$* -v tbl=$(1)_$(2)_$$* -f $(2).sql
	touch $$@
$(1)-$(2)-%.pdf: layer2img.py db/.faux_$(1)-$(2)-%
	./layer2img.py --table=$(1)_$(2)_$$* --size=$(3) --outfile $$@
crossing-$(1)-$(2)-%.pdf: layer2img.py db/.faux_$(1)-$(2)-%
	./layer2img.py --clip $(CROSSING) --table=$(1)_$(2)_$$* --size=$(3) --outfile $$@
endef

define gpkg2pdf
$(2): $(1)
	./layer2img.py $(3) --infile=$(1) --outfile $(2)
endef

$(eval $(call algo2img,sinewave,douglas,52x12))
$(eval $(call algo2img,sinewave,visvalingam,52x12))
$(eval $(call algo2img,zeimena,douglas,52x74))
$(eval $(call algo2img,zeimena,visvalingam,52x74))
$(eval $(call gpkg2pdf,sinewave.gpkg,sinewave.pdf,--size=52x15))
$(eval $(call gpkg2pdf,zeimena.gpkg,zeimena.pdf,--size=148x210 --rect $(CROSSING)))
$(eval $(call gpkg2pdf,zeimena.gpkg,crossing.pdf,--size=105x74 --clip $(CROSSING)))

sinewave.gpkg: sinewave.py
	./sinewave.py

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
