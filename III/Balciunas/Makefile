all: egzaminas-2021-01-25.pdf

%.pdf: %.tex
	latexmk -shell-escape -g -pdf $<
