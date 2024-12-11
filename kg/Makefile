LUALATEX = lualatex -shell-escape -interaction=nonstopmode -file-line-error

DELETE_FILES = *.aux *.bbl *.blg *.log *.toc *.out *.pdf *.aux
RES_DELETE_FILES = $(addprefix res/, $(DELETE_FILES))
KG1_DELETE_FILES = $(addprefix kg-i/, $(DELETE_FILES))
KG2_DELETE_FILES = $(addprefix kg-ii/, $(DELETE_FILES))
KG3_DELETE_FILES = $(addprefix kg-iii/, $(DELETE_FILES))

all: res/tree.pdf kg.pdf

view:
	xdg-open grg.pdf

kg.pdf: kg.tex
	$(LUALATEX) kg.tex
	$(LUALATEX) kg.tex

res/tree.pdf: res/tree.tex
	$(LUALATEX) --output-directory=res res/tree.tex

clean:
	rm -f $(DELETE_FILES) $(RES_DELETE_FILES) $(KG1_DELETE_FILES) $(KG2_DELETE_FILES) $(KG3_DELETE_FILES)
