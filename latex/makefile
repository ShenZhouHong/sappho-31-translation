# Makefile for latexmk
source_name = sappho-31-trans

# Makes sure latexmk always runs
.PHONY: $(source_name).pdf all clean
all: $(source_name).pdf

# MAIN LATEXMK RULE
$(source_name).pdf: $(source_name).tex
	# This makefile uses xelatex by default. This way, it supports unicode
	# characters in the latex source files. If you wish to use latex instead of
	# xelatex, simply remove the -xelatex argument
	latexmk -pdf -xelatex -use-make $<

clean:
	latexmk -c

delete:
	latexmk -C
