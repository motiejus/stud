toolshed = docker run --rm -v $(PWD):/x -w /x motiejus/toolshed

all: report.pdf

report.pdf: report.tex bib.bib
	$(toolshed) latexmk -pdf $<
