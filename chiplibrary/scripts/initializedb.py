# -*- coding: utf-8 -*-
import os
import sys
import transaction
import lxml.etree

from pyramid.paster import (
    get_appsettings,
    setup_logging
    )
from pyramid.scripts.common import parse_vars

from ..db.meta import Base
from ..db import (
    get_engine,
    get_session_factory,
    get_tm_session
    )
from ..db.chip import Chip, ChipCode

def usage(argv):
    cmd = os.path.basename(argv[0])
    print("""
    Creates tables and populates them with battle chip data using a given
    XML file.  If you need an XML dump, download `chiplibrary-data`, and 
    either use the already existing dumps/chips.xml which was pregenerated, or
    run the `spider.py` script to generate a new one.
    
    usage: %s <filename> <config_uri> [var=value]
    
    (example: "%s chips.xml config.ini")
    """ % (cmd, cmd))
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) < 3:
        usage(argv)
    filename = argv[1]
    config_uri = argv[2]
    options = parse_vars(argv[3:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    # Clear everything out first.
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine, checkfirst=True)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)
        # Parse the XML file with the chips and prepare for insertion.
        f = lxml.etree.parse(filename)

        for c in f.iter('item'):
            damage = [d.text for d in c.find('damage')]
            try:
                damage_min = damage[0]
            except IndexError:
                damage_min = '0'

            try:
                damage_max = damage[1]
            except IndexError:
                damage_max = damage_min

            chip = Chip(indice=c.find('indice').text,
                game=c.find('game').text,
                version=c.find('version').text,
                name=c.find('name').text,
                classification=c.find('classification').text,
                element=c.find('element').text,
                size=c.find('size').text,
                description=c.find('description').text,
                summary='',
                rarity=c.find('rarity').text,
                damage_min=damage_min,
                damage_max=damage_max,
                recovery=0
            )
            dbsession.add(chip)
            dbsession.flush()
            
            for code in c.find('codes'):
                dbsession.add(
                    ChipCode(
                        id_chip=chip.id,
                        code=code.text, 
                        game=c.find('game').text
                    )
                )
            dbsession.flush()
        # All done!
        print('Complete.')
