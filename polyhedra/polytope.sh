#!/bin/bash

set -ueo pipefail

cd res
echo "\documentclass[tikz, border=1mm]{standalone}" > polytope.tex
echo "\begin{document}" >> polytope.tex
sage polytope.sage >> polytope.tex
echo "\end{document}" >> polytope.tex
pdflatex polytope.tex
rm -f polytope.sage.py
cd ..
