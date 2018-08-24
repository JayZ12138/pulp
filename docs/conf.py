# -*- coding: utf-8 -*-
#
# Pulp Documentation build configuration file, created by
# sphinx-quickstart on Tue Nov 27 13:39:59 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
from datetime import date

try:
    import sphinx_rtd_theme
except ImportError:
    sphinx_rtd_theme = False

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('./_extensions'))

# Set environment variable so Sphinx can bootstrap the Django app
os.environ["DJANGO_SETTINGS_MODULE"] = "pulp.app.settings"

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['rest_api', 'sphinx.ext.extlinks']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Pulp Project'

# Set copyright to current year
copyright = u'2012-{0}, Pulp Team'.format(date.today().year)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '2.17c1'
# The full version, including alpha/beta/rc tags.
release = '2.17c1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme' if sphinx_rtd_theme else 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()] if sphinx_rtd_theme else []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'PulpDocs'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    #  The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'PulpDocs.tex', u'Pulp Documentation',
        u'Pulp Team', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('user-guide/admin-client/index', 'pulp-admin', u'Pulp Documentation', [u'Pulp Team'], 1),
    ('user-guide/consumer-client/index', 'pulp-consumer', u'Pulp Documentation', [u'Pulp Team'], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'PulpDocs', u'Pulp Documentation',
        u'Pulp Team', 'PulpDocs', 'One line description of project.',
        'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

extlinks = {'redmine': ('https://pulp.plan.io/issues/%s', '#'),
            'fixedbugs_pulp': ('https://pulp.plan.io/projects/pulp/issues?c%%5B%%5D=tracker&c%%5B%'
                               '%5D=status&c%%5B%%5D=priority&c%%5B%%5D=cf_5&c%%5B%%5D=subject&c%%'
                               '5B%%5D=author&c%%5B%%5D=assigned_to&c%%5B%%5D=cf_3&f%%5B%%5D=cf_4&'
                               'f%%5B%%5D=tracker_id&f%%5B%%5D=&group_by=&op%%5Bcf_4%%5D=%%3D&op%%'
                               '5Btracker_id%%5D=%%3D&set_filter=1&sort=priority%%3Adesc%%2Ccf_5%%'
                               '3Adesc%%2Cid%%3Adesc&utf8=%%E2%%9C%%93&v%%5Bcf_4%%5D%%5B%%5D=%s&v%'
                               '%5Btracker_id%%5D%%5B%%5D=1', 'bugs fixed in '),
            'fixedbugs_pulp_rpm': ('https://pulp.plan.io/projects/pulp_rpm/issues?c%%5B%%5D=tracke'
                                   'r&c%%5B%%5D=status&c%%5B%%5D=priority&c%%5B%%5D=cf_5&c%%5B%%5D'
                                   '=subject&c%%5B%%5D=author&c%%5B%%5D=assigned_to&c%%5B%%5D=cf_3'
                                   '&f%%5B%%5D=cf_4&f%%5B%%5D=tracker_id&f%%5B%%5D=&group_by=&op%%'
                                   '5Bcf_4%%5D=%%3D&op%%5Btracker_id%%5D=%%3D&set_filter=1&sort=pr'
                                   'iority%%3Adesc%%2Ccf_5%%3Adesc%%2Cstatus&utf8=%%E2%%9C%%93&v%%'
                                   '5Bcf_4%%5D%%5B%%5D=%s&v%%5Btracker_id%%5D%%5B%%5D=1',
                                   'bugs fixed in '),
            'fixedbugs_pulp_puppet': ('https://pulp.plan.io/projects/pulp_puppet/issues?utf8=%%E2%'
                                      '%9C%%93&set_filter=1&f%%5B%%5D=cf_4&op%%5Bcf_4%%5D=%%3D&v%%'
                                      '5Bcf_4%%5D%%5B%%5D=%s&f%%5B%%5D=tracker_id&op%%5Btracker_id'
                                      '%%5D=%%3D&v%%5Btracker_id%%5D%%5B%%5D=1&f%%5B%%5D=&c%%5B%%5'
                                      'D=tracker&c%%5B%%5D=status&c%%5B%%5D=priority&c%%5B%%5D=cf_'
                                      '5&c%%5B%%5D=subject&c%%5B%%5D=author&c%%5B%%5D=assigned_to&'
                                      'c%%5B%%5D=cf_3&group_by=', 'bugs fixed in '),
            'fixedbugs_pulp_python': ('https://pulp.plan.io/projects/pulp_python/issues?c%%5B%%5D='
                                      'tracker&c%%5B%%5D=status&c%%5B%%5D=priority&c%%5B%%5D=cf_5&'
                                      'c%%5B%%5D=subject&c%%5B%%5D=author&c%%5B%%5D=assigned_to&c%'
                                      '%5B%%5D=cf_3&f%%5B%%5D=cf_11&f%%5B%%5D=tracker_id&f%%5B%%5D'
                                      '=&group_by=&op%%5Bcf_11%%5D=%%3D&op%%5Btracker_id%%5D=%%3D&'
                                      'set_filter=1&sort=priority%%3Adesc%%2Ccf_5%%3Adesc%%2Cstatu'
                                      's&utf8=%%E2%%9C%%93&v%%5Bcf_11%%5D%%5B%%5D=%s&v%%5Btracker_'
                                      'id%%5D%%5B%%5D=1', 'bugs fixed in '),
            'fixedbugs_pulp_docker': ('https://pulp.plan.io/projects/pulp_docker/issues?utf8=%%E2%'
                                      '%9C%%93&set_filter=1&f%%5B%%5D=cf_12&op%%5Bcf_12%%5D=%%3D&v'
                                      '%%5Bcf_12%%5D%%5B%%5D=%s&f%%5B%%5D=tracker_id&op%%5Btracker'
                                      '_id%%5D=%%3D&v%%5Btracker_id%%5D%%5B%%5D=1&f%%5B%%5D=&c%%5B'
                                      '%%5D=tracker&c%%5B%%5D=status&c%%5B%%5D=priority&c%%5B%%5D='
                                      'cf_5&c%%5B%%5D=subject&c%%5B%%5D=author&c%%5B%%5D=assigned_'
                                      'to&c%%5B%%5D=cf_3&group_by=', 'bugs fixed in '),
            'fixedbugs_pulp_ostree': ('https://pulp.plan.io/projects/pulp_ostree/issues?utf8=%%E2%'
                                      '%9C%%93&set_filter=1&f%%5B%%5D=cf_17&op%%5Bcf_17%%5D=%%3D&v'
                                      '%%5Bcf_17%%5D%%5B%%5D=%s&f%%5B%%5D=tracker_id&op%%5Btracker'
                                      '_id%%5D=%%3D&v%%5Btracker_id%%5D%%5B%%5D=1&f%%5B%%5D=&c%%5B'
                                      '%%5D=tracker&c%%5B%%5D=status&c%%5B%%5D=priority&c%%5B%%5D='
                                      'cf_5&c%%5B%%5D=subject&c%%5B%%5D=author&c%%5B%%5D=assigned_'
                                      'to&c%%5B%%5D=cf_3&group_by=', 'bugs fixed in '),
            'fixedbugs_pulp_deb': ('https://pulp.plan.io/projects/pulp_deb/issues?utf8=%%E2%%9C%%93&set_'  # noqa
                                   'filter=1&f%%5B%%5D=cf_15&op%%5Bcf_15%%5D=%%3D&v%%5Bcf_15%%5D%%5B%%5D'  # noqa
                                   '=%s&f%%5B%%5D=tracker_id&op%%5Btracker_id%%5D=%%3D&v%%5Btracker_id%%'  # noqa
                                   '5D%%5B%%5D=1&f%%5B%%5D=&c%%5B%%5D=tracker&c%%5B%%5D=status&c%%5B%%5D'  # noqa
                                   '=priority&c%%5B%%5D=cf_5&c%%5B%%5D=subject&c%%5B%%5D=author&c%%5B%%5'  # noqa
                                   'D=assigned_to&c%%5B%%5D=cf_3&group_by=', 'bugs fixed in ')}
