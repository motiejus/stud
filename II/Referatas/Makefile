ZEIMENA_TOLERANCES = 100 125 250 500 1000 2000 4000
SINEWAVE_TOLERANCES = 4 5
GEN = $(addsuffix .pdf, \
		  $(addprefix sinewave-douglas-,$(SINEWAVE_TOLERANCES)) \
		  $(addprefix zeimena-douglas-,$(ZEIMENA_TOLERANCES)) \
		  $(addprefix zeimena-visvalingam-,$(ZEIMENA_TOLERANCES)))

mj-referatas.pdf: mj-referatas.tex version.tex bib.bib zeimena-pretty.pdf \
	sinewave.pdf sinewave-douglas-5.pdf $(GEN)
	latexmk -g -pdf $<

define algo2img
db/.faux_$(1)-$(2)-%: $(2).sql db/.faux_ready
	./managedb -- --echo-all -v ON_ERROR_STOP=1 -v src=$(1) -v tolerance=$$* -v tbl=$(1)_$(2)_$$* -f $(2).sql
	touch $$@

$(1)-$(2)-%.pdf: layer2img.py db/.faux_$(1)-$(2)-%
	./layer2img.py --table=$(1)_$(2)_$$* --size=52x74 --outfile $(1)-$(2)-$$*.pdf
endef

$(eval $(call algo2img,sinewave,douglas))
$(eval $(call algo2img,zeimena,douglas))
$(eval $(call algo2img,zeimena,visvalingam))

sinewave.gpkg: sinewave.py
	./sinewave.py

sinewave.pdf: sinewave.gpkg
	./layer2img.py --size=52x15 --infile=$< --outfile=$@

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
