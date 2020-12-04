all: ZPT003_2020_03_ats.txt elphistone_6.pdf

%.pdf: %.tex
	latexmk -g -lualatex $<

ZPT003_2020_03_ats.txt: ZPT003_2020_03_ats.py
	python3 $< > $@
