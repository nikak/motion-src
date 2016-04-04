#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nicolek'
SITENAME = u'motion-finder'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 12

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['docs','static', 'images', 'figure','extra/robots.txt', 'extra/favicon.ico', 'extra/static/rStyle.css']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/static/rStyle.css': {'path': 'static/rStyle.css'}
}
#from pelican.plugins import related_posts
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['gravatar','rmd_reader','series','liquid_tags','tag_cloud', 'tipue_search']
#'assets', 'sitemap',


# Specify theme
THEME = "../pelican-themes/bootstrap3"
#blue-penguin bootstrap pelican-chunk
#what follows is bootstrap3 specific
BOOTSTRAP_THEME ='readable'
CUSTOM_CSS = 'static/rStyle.css'
PYGMENTS_STYLE = 'solarizedlight'
FAVICON = 'favicon.ico'
SHOW_SERIES = True
DISPLAY_SERIES_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_SIDEBAR  = True


RMD_READER_CLEANUP = True
#RMD_READER_KNITR_QUIET = True
RMD_READER_KNITR_ENCODING = 'UTF-8'
RMD_READER_KNITR_OPTS_CHUNK = None

MARKUP = ('md', 'ipynb', 'rmd')
