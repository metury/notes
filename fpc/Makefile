LUALATEX = lualatex -shell-escape -interaction=nonstopmode -file-line-error

DELETE_FILES = *.aux *.bbl *.blg *.log *.toc *.out *.pdf *.aux *.synctex.gz
RES_DELETE_FILES = $(addprefix res/, $(DELETE_FILES))

all: res/flow.pdf fpc.pdf res/flow-dark.pdf fpc-dark.pdf

view:
	xdg-open fpc.pdf

fpc.pdf: fpc.tex
	$(LUALATEX) fpc.tex
	$(LUALATEX) fpc.tex

res/flow.pdf: res/flow.tex
	$(LUALATEX) --output-directory=res res/flow.tex

fpc-dark.pdf: fpc-dark.tex
	$(LUALATEX) fpc-dark.tex
	$(LUALATEX) fpc-dark.tex

res/flow-dark.pdf: res/flow-dark.tex
	$(LUALATEX) --output-directory=res res/flow-dark.tex

clean:
	rm -f $(DELETE_FILES) $(RES_DELETE_FILES)
