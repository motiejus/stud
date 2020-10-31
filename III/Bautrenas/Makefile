all: ZPT003_2020_01_ats.txt camberic_16.pdf camberic_6.pdf amelia_16.pdf amelia_14.pdf

%.pdf: %.tex
	latexmk -g -lualatex $<

ZPT003_2020_01_ats.txt: ZPT003_2020_01_ats.py
	python3 $< > $@
