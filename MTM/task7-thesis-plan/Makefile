toolshed ?= docker run --rm -v $(PWD):/x -w /x motiejus/toolshed

task7-thesis-plan.pdf: task7-thesis-plan.tex
	$(toolshed) latexmk -pdf $<
