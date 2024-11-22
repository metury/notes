LUALATEX = lualatex -shell-escape -interaction=nonstopmode -file-line-error

DELETE_FILES = *.aux *.bbl *.blg *.log *.toc *.out *.pdf *.aux *.synctex.gz
RES_DELETE_FILES = $(addprefix res/, $(DELETE_FILES))

all: res/sunflower.pdf selected-chapters-kg.pdf res/sunflower-dark.pdf selected-chapters-kg-dark.pdf

view:
	xdg-open selected-chapters-kg.pdf

selected-chapters-kg.pdf: selected-chapters-kg.tex
	$(LUALATEX) selected-chapters-kg.tex
	$(LUALATEX) selected-chapters-kg.tex

selected-chapters-kg-dark.pdf: selected-chapters-kg-dark.tex
	$(LUALATEX) selected-chapters-kg-dark.tex
	$(LUALATEX) selected-chapters-kg-dark.tex

res/sunflower.pdf: res/sunflower.tex
	$(LUALATEX) --output-directory=res res/sunflower.tex

res/sunflower-dark.pdf: res/sunflower-dark.tex
	$(LUALATEX) --output-directory=res res/sunflower-dark.tex
clean:
	rm -f $(DELETE_FILES) $(RES_DELETE_FILES)
