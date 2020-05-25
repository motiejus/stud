GEN = zeimena.pdf douglas-0.pdf douglas-500.pdf douglas-1000.pdf

mj-referatas.pdf: mj-referatas.tex version.tex bib.bib zeimena-pretty.pdf $(GEN)
	latexmk -g -pdf $<

zeimena.pdf: zeimena.gpkg layer2img.py
	./layer2img.py --infile=$< --size=74x52 --outfile $@

douglas-%.pdf: layer2img.py db/.faux_douglas-%
	./layer2img.py --table=douglas_$* --size=74x52 --outfile $@

db/.faux_douglas-%: db/.faux_ready douglas.sql
	./managedb -- --echo-all -v ON_ERROR_STOP=1 -v tolerance=$* -f douglas.sql
	touch $@

db/.faux_ready: zeimena.gpkg managedb
	-./managedb stop; rm -fr db
	./managedb init
	ogr2ogr -f PostgreSQL "PG:host=127.0.0.1 user=osm dbname=osm" zeimena.gpkg
	touch $@

REF = $(shell git describe --tags)
DIRTY = $(shell git status --porcelain | awk 'NR==1{print "-dirty";exit}')
GIT_DIR = $(shell git rev-parse --show-toplevel)/.git
version.tex: $(shell git ls-files .) $(GIT_DIR)
	( \
		date '+\gdef\GeneratedAt{%F %T %Z}%'; \
		printf '\gdef\VCDescribe{%s%s}%%\n' $(REF) $(DIRTY); \
	) > $@
