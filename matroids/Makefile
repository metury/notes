LUALATEX = lualatex -shell-escape -interaction=nonstopmode -file-line-error

DELETE_FILES = *.aux *.bbl *.blg *.log *.toc *.out *.pdf *.aux
RES_DELETE_FILES = $(addprefix res/, $(DELETE_FILES))

all: res/vamos.pdf matroids.pdf

view:
	firefox matroids.pdf

matroids.pdf: matroids.tex
	$(LUALATEX) matroids.tex
	$(LUALATEX) matroids.tex

res/vamos.pdf: res/vamos.tex
	$(LUALATEX) --output-directory=res res/vamos.tex

clean:
	rm -f $(DELETE_FILES) $(RES_DELETE_FILES)
