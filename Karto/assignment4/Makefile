.PHONY: all
all: KTZ004_2019_04_ats.txt teodolitinio_ejimo_resultatai.txt

KTZ004_2019_04_ats.txt: KTZ004_2019_04_ats.py measure.py 
	./$< > $@

teodolitinio_ejimo_resultatai.txt: measure.py
	./$< | column -t -s $$'\t' > $@
