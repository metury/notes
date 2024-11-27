LUALATEX = lualatex -shell-escape -interaction=nonstopmode -file-line-error

DELETE_FILES = *.aux *.bbl *.blg *.log *.toc *.out *.pdf *.aux *.synctex.gz
RES_DELETE_FILES = $(addprefix res/, $(DELETE_FILES))

all: res/sunflower.pdf selected-chapters-kg.pdf

view:
	xdg-open selected-chapters-kg.pdf

selected-chapters-kg.pdf: selected-chapters-kg.tex
	$(LUALATEX) selected-chapters-kg.tex
	$(LUALATEX) selected-chapters-kg.tex

res/sunflower.pdf: res/sunflower.tex
	$(LUALATEX) --output-directory=res res/sunflower.tex

clean:
	rm -f $(DELETE_FILES) $(RES_DELETE_FILES)
