title = 'Notes For MLCC'
filename = 'notes-for-mlcc'
outputname = 'notes-for-mlcc'

all: pdf

pdf:
	@echo "Compiling PDF file..."
	@pandoc -s $(filename).md -o $(filename).pdf \
		--title-prefix $(title) \
		--listings -H meta/py-listing.tex \
		--template=meta/template.tex \
		-f markdown+smart \
		--pdf-engine=`which xelatex`
	@echo "Done."
	@rm *.md

markdown:
	@echo "Copy markdown assets"
	@cp -r ../notes/assets/ . 
	@echo "Merge markdown files..."
	@python3 merge_md.py

clean:
	rm -rf *.md *.pdf assets/

.PHONY: markdown pdf clean