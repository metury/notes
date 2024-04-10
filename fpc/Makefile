LUALATEX = lualatex -shell-escape -interaction=nonstopmode -file-line-error

DELETE_FILES = *.aux *.bbl *.blg *.log *.toc *.out *.pdf *.aux
RES_DELETE_FILES = $(addprefix res/, $(DELETE_FILES))

all: res/flow.pdf fpc.pdf

view:
	firefox fpc.pdf

fpc.pdf: fpc.tex
	$(LUALATEX) fpc.tex
	$(LUALATEX) fpc.tex

res/flow.pdf: res/flow.tex
	$(LUALATEX) --output-directory=res res/flow.tex

clean:
	rm -f $(DELETE_FILES) $(RES_DELETE_FILES)
