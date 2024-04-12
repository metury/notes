LUALATEX = lualatex -shell-escape -interaction=nonstopmode -file-line-error

DELETE_FILES = *.aux *.bbl *.blg *.log *.toc *.out *.pdf *.aux
RES_DELETE_FILES = $(addprefix res/, $(DELETE_FILES))

all: res/polytope.pdf polyhedra.pdf

view:
	firefox polyhedra.pdf

polyhedra.pdf: polyhedra.tex
	$(LUALATEX) polyhedra.tex
	$(LUALATEX) polyhedra.tex

res/polytope.pdf: polytope.sh
	./polytope.sh

clean:
	rm -f $(DELETE_FILES) $(RES_DELETE_FILES) res/polytope.tex
