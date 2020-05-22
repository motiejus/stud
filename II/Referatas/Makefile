SHELL = /bin/bash

GEN = zeimena.pdf st-simplify-100.pdf st-simplify-150.pdf st-simplify-300.pdf st-simplify-500.pdf

mj-referatas.pdf: mj-referatas.tex version.tex bib.bib zeimena-pretty.pdf $(GEN)
	latexmk -g -pdf $<

zeimena.pdf: zeimena.gpkg
	./layer2img.py --infile=$< --size=74x52 --outfile $@

st-simplify-%.pdf: db/.faux_st-simplify-%
	./layer2img.py --table=douglas_$* --size=74x52 --outfile $@

db/.faux_st-simplify-%: db/.faux_ready st-simplify.sql
	. ./managedb ; \
		psql --echo-all -v ON_ERROR_STOP=1 -v tolerance=$* -f st-simplify.sql
	touch $@

db/.faux_ready: zeimena.gpkg managedb
	-./managedb stop; rm -fr db
	./managedb init
	ogr2ogr -f PostgreSQL "PG:host=127.0.0.1 user=osm dbname=osm" zeimena.gpkg
	touch $@

GIT_DIR = $(shell git rev-parse --show-toplevel)/.git

version.tex: $(shell git ls-files .) $(GIT_DIR)
	date "+%F %T %Z" | awk '{print "\\gdef\\GeneratedAt{"$$0"}%"}' > $@
	[ -n "$$(git status --porcelain)" ] && suffix="-dirty"; \
		git describe --tags | awk '{print "\\gdef\\VCDescribe{"$$0"'$$suffix'}%"}' >> $@
