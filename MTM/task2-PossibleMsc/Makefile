ifdef IN_DOCKER
toolshed = docker run --rm -v $(PWD):/x -w /x motiejus/toolshed
endif

report.pdf: report.tex
	$(toolshed) latexmk $<
