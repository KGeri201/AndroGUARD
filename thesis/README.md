LaTeX template for bachelor's thesis at IAIK
============================================

This is a simple LaTeX template for **bachelor's theses** and **master's project reports** at IAIK.
(For master's theses, see links at the bottom.)
Using this template is *optional*; feel free to tinker with the details.

Contents
--------

This template contains the following files ([download zip](https://extgit.iaik.tugraz.at/castle/student/templates/bachelor-thesis/-/archive/master/bachelor-thesis-master.zip?path=thesis)):

  * `iaikthesis.sty`: Defines the LaTeX style and title page - do not edit. This style is derived from the official TU Graz title page for master's theses and adapted to support bachelor's theses and master's projects, including IAIK-specific details.

  * `thesis.tex`: LaTeX file that you can use as a starting template for your thesis. Includes some writing tips and various other packages that you may find useful in the comments.
     You may want to create and include additional `.tex` files using `\input{...}` (e.g., for each chapter) to structure your content.

  * `thesis.bib`: BibTeX file with example bibliography entries. Edit to include your own references. You can find bibliographic details for papers on [DBLP Computer Science Bibliography](https://dblp.org/search/) or [Google Scholar](https://scholar.google.com/).

  * `Makefile`: For building `thesis.pdf` (see below).

  * `README.md`: This file.

How to use
----------

You can use `make` to build `thesis.pdf` and `make clean` to remove temporary files from the build process. Requires `latexmk`.

Alternatively, compile manually as follows:

```bash
pdflatex thesis.tex
biber thesis
pdflatex thesis.tex
```

If you have troubles compiling the bibliography in your setup (e.g., because your IDE doesn't support `biber`), edit `thesis.tex` and replace `backend=biber` by `backend=bibtex`. Then you can compile the bibliography with `bibtex thesis` instead of `biber thesis`, though this comes with some limitations.

Links
-----

  * [IAIK bachelor's thesis](https://extgit.iaik.tugraz.at/castle/student/templates/bachelor-thesis)
  * [IAIK master's project](https://extgit.iaik.tugraz.at/castle/student/templates/master-project)
  * [IAIK master's thesis](https://extgit.iaik.tugraz.at/castle/student/templates/master-thesis), based on the [TU Graz thesis titlepage](https://tu4u.tugraz.at/en/students/organisation-and-administration/corporate-design-templates/#c252670)
  * [TU Graz presentations](https://tu4u.tugraz.at/en/students/organisation-and-administration/corporate-design-templates/#c248569) ([LaTeX](https://tu4u.tugraz.at/en/students/organisation-and-administration/corporate-design-templates/latex-presentation-template/) or [Powerpoint](https://tu4u.tugraz.at/en/students/organisation-and-administration/corporate-design-templates/minimalist-powerpoint-presentation-template-with-more-space-for-content/))

Contact
-------

maria.eichlseder@iaik.tugraz.at
