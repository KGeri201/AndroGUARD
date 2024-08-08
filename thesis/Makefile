BASEFILE ?= thesis

.PHONY: all view clean

all:
	latexmk -pdf --interaction=nonstopmode -halt-on-error -synctex=1 -file-line-error $(BASEFILE).tex

view:
	xdg-open $(BASEFILE).pdf

clean:
	@rm -f *.aux
	@rm -f *.bbl
	@rm -f *.bcf
	@rm -f *.blg
	@rm -f *.fdb_latexmk
	@rm -f *.fls
	@rm -f *.ist
	@rm -f *.lof
	@rm -f *.log
	@rm -f *.lot
	@rm -f *.out
	@rm -f *.run.xml
	@rm -f *.synctex.gz
	@rm -f *.tdo
	@rm -f *.toc
