title = 'Notes For MLCC'
filename = 'notes-for-mlcc'
outputname = 'notes-for-mlcc'

all: markdown
	 pdf

pdf:
	@echo "Compiling PDF file..."
	@pandoc -s $(filename).md -o $(filename).pdf \
		--title-prefix $(title) \
		--template=meta/template.tex \
		--listings \
		-f markdown+smart-implicit_figures \
		--pdf-engine=`which xelatex`
	@echo "Done."
	@rm *.md assets/

markdown:
	@echo "Copy markdown assets"
	@cp -r ../notes/assets/ ./assets/ 
	@echo "Merge markdown files..."
	@python3 merge_md.py

clean:
	rm -rf *.md *.pdf assets/

.PHONY: markdown pdf clean