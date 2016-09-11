chiplibrary
==================

Preamble
---------------
chiplibrary is a personal project of mine that attempts to create a comprehensive index of the battle chips from the Mega Man Battle Network series.  Unless you play MMBN or are a fan of data mining, this will all be useless to you, but I have provided the code for it in hopes that it may be useful to someone for something, whether it just be the database itself or other pieces of code.

Requirements
---------------
- pyramid
- sqlalchemy
- mako
- webhelpers2
- mistune (markdown parser used for chip summary sections)
- libsass (optional: if you wish to edit and compile the CSS)
- virtualenv (optional: if you want to setup your own environment)

Setup
---------------
Before getting chiplibrary running, you need data to populate the database, which is where [chiplibrary-data](https://github.com/chrisrsantiago/chiplibrary-data) comes into play.  Assuming you have `git` installed, retrieving data should be as simple as cloning the repo and using the already existing *dumps/chips.xml* file present.  `scrapy` is completely optional unless you plan to run the spider:

`git clone https://github.com/chrisrsantiago/chiplibrary-data.git`

If you haven't already, make sure to edit *sqlalchemy.url* to reflect what database you want to use.  Since there is
no migration (as of yet,) all previous chip_* tables are automatically dropped before the databse is populated with data.  In order to avoid UnicodeErrors, the character set and connection type should always be unicode (utf8).  More information is available in the sample `config.ini` provided.

`cd /directory/containing/this/file`
`$VENV/bin/python3 setup.py develop`
`$VENV/bin/initialize_chiplibrary_db /path/to/your/chips.xml config.ini`
`$VENV/bin/pserve config.ini`

Using Sass/SCSS
---------------
chiplibrary uses Sass for its stylesheets.  You can compile the stylesheets using whichever compiler you'd like, but if you prefer to use Python:

`rm -rf static/css; python -c "import sass; sass.compile(dirname=['scss', 'static/css'])"`
