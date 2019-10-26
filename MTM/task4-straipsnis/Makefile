toolshed = docker run --rm -v $(PWD):/x -w /x motiejus/toolshed

all: straipsnis.html

straipsnis.html: straipsnis.md
	$(toolshed) pandoc \
		-T "$(shell head -1 $<)" \
		--self-contained $< -o $@
