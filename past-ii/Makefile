LUALATEX = lualatex -shell-escape -interaction=nonstopmode -file-line-error

DELETE_FILES = *.aux *.bbl *.blg *.log *.toc *.out *.pdf *.aux
RES_DELETE_FILES = $(addprefix res/, $(DELETE_FILES))

all: res/past-ii.pdf past-ii.pdf

view:
	firefox past-ii.pdf

past-ii.pdf: past-ii.tex
	$(LUALATEX) past-ii.tex
	$(LUALATEX) past-ii.tex

res/past-ii.pdf: res/past-ii.tex
	$(LUALATEX) --output-directory=res res/past-ii.tex

clean:
	rm -f $(DELETE_FILES) $(RES_DELETE_FILES)
