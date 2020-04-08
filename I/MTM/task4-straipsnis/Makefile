toolshed = docker run --rm -v $(PWD):/x -w /x motiejus/toolshed

all: README.html

README.html: README.md
	$(toolshed) pandoc \
		-T "$(shell head -1 $<)" \
		--self-contained $< -o $@
