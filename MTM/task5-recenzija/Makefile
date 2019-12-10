toolshed ?= docker run --rm -v $(PWD):/x -w /x motiejus/toolshed

task5-recenzija.pdf: task5-recenzija.tex bib.bib
	$(toolshed) latexmk -pdf $<
