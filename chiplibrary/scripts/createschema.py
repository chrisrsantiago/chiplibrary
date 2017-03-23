# -*- coding: utf-8 -*-
import os
import sys
import transaction

from pyramid.paster import get_appsettings, setup_logging
from pyramid.scripts.common import parse_vars

from social.apps.pyramid_app.models import init_social

from ..db import get_session
from ..db.meta import Base

from ..lib.auth import SOCIAL_AUTH_SETTINGS

def usage(argv):
    cmd = os.path.basename(argv[0])
    print("""
    Drops all database tables and creates them once again.
    
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
    settings = get_appsettings(config_uri, options=options)
    dbsession = get_session(settings)
    engine = dbsession.get_bind()
    init_social(SOCIAL_AUTH_SETTINGS, Base, dbsession)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine, checkfirst=True)
    print('All done!')
    sys.exit(1)
