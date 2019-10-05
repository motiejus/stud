toolshed = docker run --rm -v $(PWD):/x -w /x motiejus/toolshed

task3-EpisodeAnalysis.pdf: task3-EpisodeAnalysis.tex bib.bib
	$(toolshed) latexmk -pdf $<
