LUALATEX = lualatex -shell-escape -interaction=nonstopmode -file-line-error

DELETE_FILES = *.aux *.bbl *.blg *.log *.toc *.out *.pdf *.aux
RES_DELETE_FILES = $(addprefix res/, $(DELETE_FILES))

all: res/venn.pdf temno.pdf

view:
	xdg-open fpc.pdf

temno.pdf: temno.tex
	$(LUALATEX) temno.tex
	$(LUALATEX) temno.tex

res/venn.pdf: res/venn.tex
	$(LUALATEX) --output-directory=res res/venn.tex

clean:
	rm -f $(DELETE_FILES) $(RES_DELETE_FILES)
