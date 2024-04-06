LUALATEX = lualatex -shell-escape -interaction=nonstopmode -file-line-error

all: grg.pdf

view:
	firefox grg.pdf

grg.pdf: grg.tex
	$(LUALATEX) grg.tex
	$(LUALATEX) grg.tex

clean:
	rm -f *.aux *.bbl *.blg *.log *.toc *.out *.pdf