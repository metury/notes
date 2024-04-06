LUALATEX = lualatex -shell-escape -interaction=nonstopmode -file-line-error

all: matroids.pdf

view:
	firefox matroids.pdf

matroids.pdf: matroids.tex
	$(LUALATEX) matroids.tex

matroids.aux: matroids.tex
	$(LUALATEX) matroids.tex

clean:
	rm -f *.aux *.bbl *.blg *.log *.fmt *.pdf