# -*- coding: utf-8 -*-
import os
import sys
import logging
import transaction

from pyramid.paster import get_appsettings, setup_logging
from pyramid.scripts.common import parse_vars

from ..db import get_session
from ..db.chip import Chip, ChipCode
from ..lib.search import Library

def usage(argv):
    cmd = os.path.basename(argv[0])
    print("""
    Builds Whoosh indexes for search engine purposes, and purges the old one.

    usage: %s <config_uri> [var=value]

    (example: "%s config.ini")
    """ % (cmd, cmd))
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    log = logging.getLogger(__name__)
    settings = get_appsettings(config_uri, options=options)
    settings['config_path'] = os.path.dirname(config_uri)
    settings['whoosh.rebuild'] = 'true'
    # Setup SQLAlchemy
    dbsession = get_session(settings)
    # Rebuild Indexes
    log.info('Rebuilding index')
    library = Library(dbsession, **settings)
    # All done!
    log.info('Rebuilding Complete')
