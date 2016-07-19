chiplibrary
==================

Preamble
---------------
chiplibrary is

Requirements
---------------
- pyramid
- sqlalchemy
- mako
- webhelpers2
- libsass (optional: if you wish to edit and compile the CSS)
- virtualenv (optional: if you want to setup your own environment)
- scrapy (optional: if you want to run the web spiders)

Setup
---------------
Once this project is actually done, I'll put together a real installation process, but for now...

If you haven't already, make sure to edit the *mako.directories* directive in your
.ini configuration file to reflect where the templates are being stored, and your *sqlalchemy.url* to reflect what database you want to use.  Since there is
no migration (as of yet,) make sure that the database is empty.

`cd /directory/containing/this/file`
`$VENV/bin/pip install -e .`
`$VENV/bin/initialize_chiplibrary_db config.ini`
`$VENV/bin/pserve config.ini`

Using Sass/SCSS
---------------
chiplibrary uses Sass for its stylesheets.  You can compile the stylesheets using whichever compiler you'd like, but if you prefer to use python:

`rm -rf static/css; python -c "import sass; sass.compile(dirname=['scss', 'static/css'])"`
