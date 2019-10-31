toolshed = docker run --rm -v $(PWD):/x -w /x motiejus/toolshed

thesisMJ-memo.pdf: thesisMJ-memo.tex bib.bib 
	$(toolshed) latexmk -pdf $<
