# -*- coding: utf-8 -*-
import os
import sys
import transaction
import logging
import lxml.etree

from pyramid.paster import get_appsettings, setup_logging
from pyramid.scripts.common import parse_vars

from ..db import get_session
from ..db.chip import Chip, ChipCode

def usage(argv):
    cmd = os.path.basename(argv[0])
    print("""
    Populates chip tables with battle chip data using a given
    XML file.  If you need an XML dump, download `chiplibrary-data`, and 
    either use the already existing dumps/chips.xml which was pregenerated, or
    run the `scrapy runspider spider.py` script to generate a new one.

    usage: %s <config_uri> <filename> [var=value]

    (example: "%s config.ini chips.xml")
    """ % (cmd, cmd))
    sys.exit(1)

def main(argv=sys.argv):
    if len(argv) < 3:
        usage(argv)
    config_uri = argv[1]
    filename = argv[2]
    options = parse_vars(argv[3:])
    setup_logging(config_uri)
    log = logging.getLogger(__name__)
    settings = get_appsettings(config_uri, options=options)
    dbsession = get_session(settings)
    log.info('Loading battlechips...')
    with transaction.manager:
        # Clear out our chip database.
        dbsession.query(Chip).delete()
        dbsession.query(ChipCode).delete()
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

            try:
                size = int(c.find('size').text)
            except TypeError:
                size = 0

            chip = Chip(
                indice=c.find('indice').text,
                indice_game=c.find('indice_game').text,
                game=c.find('game').text,
                version=c.find('version').text,
                name=c.find('name').text,
                name_jp=c.find('name_jp').text,
                classification=c.find('classification').text,
                element=c.find('element').text,
                size=size,
                description=c.find('description').text,
                summary='',
                rarity=int(c.find('rarity').text),
                damage_min=int(damage_min),
                damage_max=int(damage_max),
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
        log.info('Loading battlechips complete')
