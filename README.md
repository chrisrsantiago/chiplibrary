chiplibrary
==================

Preamble
---------------
chiplibrary is a personal project of mine that attempts to create a comprehensive index of the battle chips from the Mega Man Battle Network series.  Unless you play MMBN or are a fan of data mining, this will all be useless to you, but I have provided the code for it in hopes that it may be useful to someone for something, whether it just be the database itself or other pieces of code.

To see chiplibrary in action, check the official website:

[http://chiplibrary.net/](http://chiplibrary.net/)

Any and all bug reports should be submitted via the [https://github.com/chrisrsantiago/chiplibrary/issues](Issues) tab on the official Github.

Requirements
---------------
- Python >= 3.2
- pyramid
- pyramid_dogpile_cache2
- sqlalchemy
- mako
- whoosh
- webhelpers2
- python-social-auth
- wtforms
- inflect
- munch
- mistune (markdown parser used for chip summaries and articles)
- Sass (optional: if you wish to edit and compile the CSS)
- virtualenv (optional: if you want to setup your own Python development environment)


Using Sass/SCSS
---------------
chiplibrary uses Sass for its stylesheets.  By default, the stylesheets are already compiled to CSS, and ready to use, so it is not necessary.  All relevant stylesheets can be found in the `chiplibrary/scss` directory.  You may compile the stylesheets using whichever Sass compiler you wish.

Setup
---------------
Before getting chiplibrary running, you need data to populate the database, which is where [chiplibrary-data](https://github.com/chrisrsantiago/chiplibrary-data) comes into play.  Assuming you have `git` installed, retrieving data should be as simple as cloning the repo and using the already existing *dumps/chips.xml* file present.  `scrapy` is completely optional unless you plan to run the spider:

`git clone https://github.com/chrisrsantiago/chiplibrary-data.git`

If you haven't already, make sure to edit *sqlalchemy.url* to reflect what database you want to use.  Since there is
no migration (as of yet,) all previous chip_* tables are automatically dropped before the database is populated with data.  In order to avoid UnicodeErrors, the character set and connection type should always be unicode (utf8).

More information is available in the sample `config.ini` provided.

Run the setup to install all dependencies and setup the `chiplibrary` package.  `setup.py develop` will setup an .egg-link pointing to the current directory, so you will be able to make changes to any files in chiplibrary and test them out.

`cd /directory/containing/this/file`

`$VENV/bin/python3 setup.py develop`

Create your schema.  This will delete any already existing data:

`$VENV/bin/chiplibrary_createschema config.ini`

Assuming that was a success, it's time to populate the database with data.  Using your chips.xml dump with the `chiplibrary_loadchips` script:

`$VENV/bin/chiplibrary_loadchips config.ini /path/to/your/chips.xml`

After the data has been populated successfully, it's time to build the search engine index to allow for the search feature to work:

`$VENV/bin/chiplibrary_buildindex config.ini`

Once that's done, you should be good to go, and you can run the server.  However you want to deploy is up to you, but for your own purposes this will suffice:

`$VENV/bin/pserve config.ini`

Enjoy!
