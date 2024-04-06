LUALATEX = lualatex -shell-escape -interaction=nonstopmode -file-line-error

DELETE_FILES = *.aux *.bbl *.blg *.log *.toc *.out *.pdf *.aux
RES_DELETE_FILES = $(addprefix res/, $(DELETE_FILES))
GRG1_DELETE_FILES = $(addprefix grg-i/, $(DELETE_FILES))
GRG2_DELETE_FILES = $(addprefix grg-ii/, $(DELETE_FILES))

all: res/filament.pdf grg.pdf

view:
	firefox grg.pdf

grg.pdf: grg.tex
	$(LUALATEX) grg.tex
	$(LUALATEX) grg.tex

res/filament.pdf: res/filament.tex
	$(LUALATEX) --output-directory=res res/filament.tex

clean:
	rm -f $(DELETE_FILES) $(RES_DELETE_FILES) $(GRG1_DELETE_FILES) $(GRG2_DELETE_FILES)
