mj-praktika.pdf: mj-praktika.tex version.tex
	latexmk -g -pdf $<

REF = $(shell git describe --tags --dirty)
GIT_DIR = $(shell git rev-parse --show-toplevel)/.git
version.tex: $(shell git ls-files .) $(GIT_DIR)
	( \
		date '+\gdef\GeneratedAt{%F %T %Z}%'; \
		printf '\gdef\VCDescribe{%s}%%\n' $(REF); \
	) > $@
