LUALATEX = lualatex -shell-escape -interaction=nonstopmode -file-line-error

DELETE_FILES = *.aux *.bbl *.blg *.log *.toc *.out *.pdf *.aux
RES_DELETE_FILES = $(addprefix res/, $(DELETE_FILES))

all: res/sunflower.pdf vybrane-kapitoly-kg.pdf

view:
	xdg-open vybrane-kapitoly-kg.pdf

vybrane-kapitoly-kg.pdf: vybrane-kapitoly-kg.tex
	$(LUALATEX) vybrane-kapitoly-kg.tex
	$(LUALATEX) vybrane-kapitoly-kg.tex

res/sunflower.pdf: res/sunflower.tex
	$(LUALATEX) --output-directory=res res/sunflower.tex

clean:
	rm -f $(DELETE_FILES) $(RES_DELETE_FILES)
