SHELL = /bin/bash -eu
.SECONDARY:
.DELETE_ON_ERROR:

-include Makefile.local

presentation-skim.pdf:

%-skim.pdf: %.pdf
	cp $< $@

%.pdf: %.tex
	rubber -m graphics -m xelatex --warn=refs --warn=misc presentation.tex
