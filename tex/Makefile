FILE=antsystem

all:
	pdflatex $(FILE).tex
	bibtex $(FILE)
	pdflatex $(FILE).tex
	pdflatex $(FILE).tex 

clean:
	rm -f *.log *.aux *.bbl *.blg
