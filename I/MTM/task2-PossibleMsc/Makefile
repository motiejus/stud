ifdef IN_DOCKER
toolshed = docker run --rm -v $(PWD):/x -w /x motiejus/toolshed
endif

all: report1.pdf report2.pdf

report%.pdf: report%.tex
	$(toolshed) latexmk -pdf $<
