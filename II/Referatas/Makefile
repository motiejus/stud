TOLERANCES = 0 500 1000 2000 4000
GEN = $(addsuffix .pdf,zeimena \
		  $(addprefix douglas-,$(TOLERANCES)) \
		  $(addprefix visvalingam-,$(TOLERANCES)))

mj-referatas.pdf: mj-referatas.tex version.tex bib.bib zeimena-pretty.pdf $(GEN)
	latexmk -g -pdf $<

zeimena.pdf: zeimena.gpkg layer2img.py
	./layer2img.py --infile=$< --size=74x52 --outfile $@

define algo2img
db/.faux_$(1)-$(2): $(1).sql db/.faux_ready
	./managedb -- --echo-all -v ON_ERROR_STOP=1 -v tolerance=$(2) -f $(1).sql
	touch db/.faux_$(1)-$(2)

$(1)-$(2).pdf: layer2img.py db/.faux_$(1)-$(2)
	./layer2img.py --table=$(1)_$(2) --size=52x74 --outfile $(1)-$(2).pdf
endef

$(foreach t,$(TOLERANCES),$(eval $(call algo2img,douglas,$(t))))
$(foreach t,$(TOLERANCES),$(eval $(call algo2img,visvalingam,$(t))))

db/.faux_ready: zeimena.gpkg managedb
	-./managedb stop; rm -fr db
	./managedb init
	ogr2ogr -f PostgreSQL "PG:host=127.0.0.1 user=osm dbname=osm" $<
	touch $@

REF = $(shell git describe --tags)
DIRTY = $(shell git status --porcelain | awk '{print"-dirty";exit}')
GIT_DIR = $(shell git rev-parse --show-toplevel)/.git
version.tex: $(shell git ls-files .) $(GIT_DIR)
	( \
		date '+\gdef\GeneratedAt{%F %T %Z}%'; \
		printf '\gdef\VCDescribe{%s%s}%%\n' $(REF) $(DIRTY); \
	) > $@
