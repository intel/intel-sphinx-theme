# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

html:
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)"/html $(SPHINXOPTS) $(O)
	mkdir -p "$(BUILDDIR)"/html/_static
	cp _static/switcher.json "$(BUILDDIR)"/html/_static/switcher.json
	cp _static/redirects/guide-homepage-redirect.html "$(BUILDDIR)"/html/index.html

.PHONY: html-cb html-tb html-all

html-cb:
	SUBTHEME="default" $(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)/html/default $(SPHINXOPTS) $(O)
	mkdir -p "$(BUILDDIR)"/html/_static
	cp _static/switcher.json $(BUILDDIR)/html/_static/switcher.json
	cp _static/redirects/guide-homepage-redirect.html $(BUILDDIR)/html/default/index.html
	echo '<!DOCTYPE html><html><head><meta http-equiv="refresh" content="0; url=default/"></head></html>' > "$(BUILDDIR)"/html/index.html

html-tb:
	SUBTHEME="tb" $(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)/html/tb $(SPHINXOPTS) $(O)
	mkdir -p "$(BUILDDIR)"/html/_static
	cp _static/switcher.json $(BUILDDIR)/html/_static/switcher.json
	cp _static/redirects/guide-homepage-redirect.html $(BUILDDIR)/html/tb/index.html

html-all: html-cb html-tb

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)