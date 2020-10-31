all: camberic_16.pdf camberic_6.pdf amelia_16.pdf amelia_14.pdf

%.pdf: %.tex
	latexmk -g -lualatex $<
