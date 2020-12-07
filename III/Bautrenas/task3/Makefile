all: ZPT003_2020_03_ats.txt elphistone_6.pdf

%.pdf: %.tex
	latexmk -g -lualatex $<

ZPT003_2020_03_ats.txt: ZPT003_2020_03_ats.py consts.py
	python3 $< > $@

consts.py: elphistone_6.pdf
	printf "wc = %d\n" $$(pdftotext $< - | wc -m) > $@
