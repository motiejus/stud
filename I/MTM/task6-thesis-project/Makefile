toolshed ?= docker run --rm -v $(PWD):/x -w /x motiejus/toolshed

task6-thesis-project.pdf: task6-thesis-project.tex bib.bib
	$(toolshed) latexmk -pdf $<
