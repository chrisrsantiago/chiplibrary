# -*- coding: utf-8 -*-
"""Grabs battle chip data from relevant wiki pages.  This is not necessary
or useful to you unless you enjoy coding, or seeing how other people do things,
but I've included it anyway.

Because of the incomplete nature of the online resources, coupled with my
laziness, this doesn't create a complete, ready-to-import-to-the-database dump
YET.

Using the spiders
---------------
scrapy runspider mmkb.py -a game=`game` -classification=`classification`

`game` can be bn1, bn2, bn3, bn4, bn5, bn6 (Default: bn1)
`classification` can be mega, giga, secret, dark (Default: blank)

(By default, unless specified in the -classification argument, only
standard chips will be grabbed.)

If you want it to output to a file, simply pass the -o argument with a filename
and extension compatible with scrapy's feed exporters, or your own if you have
written one:

https://scrapy.readthedocs.io/en/latest/topics/feed-exports.html


If you want to learn more about using scrapy,
read the [scrapy docs](http://scrapy.org/docs/).
"""
import sys
import re
import urllib.request

import scrapy
from scrapy import signals
from scrapy.loader.processors import TakeFirst
from scrapy.exporters import XmlItemExporter

def bn1_getattrs():
    """MMKB is missing information such as stars, elements and chip codes from
    MMBN1, so this function grabs the entire chip catalog from a user-compiled
    list on GameFAQs to add to the exported item. (Credit: Geoff Mendicino)
    
    Returns a dict 
    """
    re_faqformat = re.compile(r"""
        ([0-9]+)[\s]+([A-Z-0-9-\-]+)
        [\s]+([A-Z]+)
        [\s]+([0-9-\???\\+\\*]+)
        [\s]+([0-9]+)
        [\s]+([A-Z-\*]+)""",
        re.DOTALL | re.VERBOSE | re.IGNORECASE
    )
    req = urllib.request.Request(
        'https://www.gamefaqs.com/gba/457634-mega-man-battle-network/faqs/30244?print=1',
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    with urllib.request.urlopen(req) as resp:
        chips = {}
        for chip in re.findall(re_faqformat, str(resp.read())):
            # Create a dict that can be referenced with the chip indice
            # with a tuple containing the element, stars and chip codes
            chips['%s' % (chip[0],)] = (
                chip[2].lower() \
                    .replace('water', 'aqua') \
                    .replace('elec', 'electric') \
                    .replace('none', 'null'),
                chip[4],
                list(chip[5])
            )
        return chips

class ChipsItem(scrapy.Item):
    default_output_processor = TakeFirst()
    
    description = scrapy.Field()
    indice = scrapy.Field()
    name = scrapy.Field()
    element = scrapy.Field()
    size = scrapy.Field()
    codes = scrapy.Field()
    classification = scrapy.Field()
    power = scrapy.Field()
    stars = scrapy.Field()
    game = scrapy.Field()

class FormatterPipeline(object):
    """Formats data properly.
    """
    
    def process_item(self, item, spider):
        item['name'] = item['name'][0]
        item['indice'] = item['indice'][0].lstrip('0')
        
        if item['size']:
            item['size'] = item['size'][0].replace(' MB', '').strip()

        if item['power']:
            # MMBN and OSS have the same chips. We don't care about the
            # OSS data, so ignore it.
            if spider.game in ('bn1') and len(item['power']) > 1:
                power_re = re.compile(u'([0-9]+)\s\(MMBN\)')
                result_re = power_re.match(item['power'][0])
                item['power'] = result_re.group(1)
            item['power'] = item['power'][0]
            # todo: handle recovery chips and chips with no predefined
            # damage.
            if item['power'] == '-':
                item['power'] = 0

        if item['codes']:
            # Remove whitespace and convert into a list.
            if spider.game in ('bn2', 'bn3'):
                item['codes'] = list(
                    map(unicode.strip, item['codes'].split(','))
                )
            # Separate chip code from the locations
            if spider.game in ('bn4', 'bn5', 'bn6'):
                code_re = re.compile(u'([A-Z-\*]):', re.MULTILINE)
                item['codes'] = code_re.findall(item['codes'])
        
        item['description'] = item['description'][0].strip()
        return item

class MegaSpider(scrapy.Spider):
    name = 'chiplibrary'
    allowed_domains = ['megaman.wikia.com']

    custom_settings = {
        'ITEM_PIPELINES': {
            'chiplibrary.spiders.mmkb.FormatterPipeline': 1
        }
    }

    xpaths = {
        'bn1': {
            'table': '//*[@id="mw-content-text"]/table[1]',
            'indice': 'td[1]/text()',
            'name': 'td[3]/text()',
            'power': 'td[4]/text()',
            'description': 'td[5]/text()',
            'size': '',
            'codes': ''
         },
        'bn2': {
            'table': '//*[@id="mw-content-text"]/table[1]',
            'indice': 'td[1]/text()',
            'name': 'td[3]/text()',
            'element': 'td[4]/a/img/@alt',
            'power': 'td[5]/text()',
            'codes': 'td[6]/text()',
            'size': 'td[7]/text()',
            'description': 'td[8]/text()'
         },
        'bn3': {
            'table': '//*[@id="mw-content-text"]/table[1]',
            'table_mega': '//*[@id="mw-content-text"]/table[2]',
            'table_giga': '//*[@id="mw-content-text"]/table[3]',
            'indice': 'td[1]/text()',
            'name': 'td[3]/text()',
            'power': 'td[4]/text()',
            'codes': 'td[5]/text()',
            'size': 'td[6]/text()',
            'description': 'td[7]/text()'
        },
        'bn4': {
            'table': '//*[@id="mw-content-text"]/table[2]',
            'table_mega': '//*[@id="mw-content-text"]/table[3]',
            'table_giga': '//*[@id="mw-content-text"]/table[4]',
            'table_secret': '//*[@id="mw-content-text"]/table[5]',
            'indice': 'td[1]/text()',
            'name': 'td[3]/text()',
            'power': 'td[4]/text()',
            'size': 'td[5]/text()',
            'description': 'td[6]/text()'
        },
        'bn5': {
            'table': '//*[@id="mw-content-text"]/table[1]',
            'table_mega': '//*[@id="mw-content-text"]/table[2]',
            'table_giga': '//*[@id="mw-content-text"]/table[4]',
            'table_secret': '//*[@id="mw-content-text"]/table[3]',
            'table_dark': '//*[@id="mw-content-text"]/table[5]',
            'indice': 'td[1]/text()',
            'name': 'td[3]/text()',
            'power': 'td[4]/text()',
            'codes': 'td[5]/text()',
            'size': 'td[6]/text()',
            'description': 'td[7]/text()'
        },
        'bn6': {
            'table': '//*[@id="mw-content-text"]/table[1]',
            'table_mega': '//*[@id="mw-content-text"]/table[2]',
            'table_giga': '//*[@id="mw-content-text"]/table[3]',
            'indice': 'td[1]/text()',
            'name': 'td[3]/text()',
            'element': 'td[4]/a/img/@alt',
            'power': 'td[5]/text()',
            'description': 'td[6]/text()',
            'size': '',
            'codes': ''
        }
    }

    def __init__(self, game='bn1', classification=''):
        self.game = game
        page = self.game.replace('bn', '_')
        if self.game == 'bn1':
            page = ''
            
        self.start_urls = [
            'http://megaman.wikia.com/wiki/List_of_Mega_Man_Battle_Network%s_Battle_Chips' % (page,)
        ]
        # Chip Classifications are introduced post-MMBN2, secret chips
        # are only available in MMBN4-5, and dark chips are only available in
        # MMBN5.
        self.classification = ''
        
        if (classification and (
                (
                    classification in ('mega', 'giga', 'secret')
                    and game in ('bn3', 'bn4', 'bn5', 'bn6')
                )
                or (classification == 'secret' and game in ('bn4', 'bn5'))
                or (classification == 'dark' and game == 'bn5')
            )
        ):
            self.classification = classification

    def parse(self, response):
        xpaths = self.xpaths[self.game]
        xpaths_classification = 'table'

        if self.classification:
            xpaths_classification = 'table_%s' % (self.classification)

        if self.game == 'bn1':
            _bn1_attrs = bn1_getattrs()

        for sel in response.xpath(
            '%s/tr[position()>1]' % (xpaths[xpaths_classification],)
        ):
            item = ChipsItem()
            item['game'] = self.game
            item['description'] = sel.xpath(xpaths['description']).extract()
            item['indice'] = sel.xpath(xpaths['indice']).extract()
            
            # There is probably a hyperlink preventing us from grabbing the
            # chip name.
            item['name'] = sel.xpath(xpaths['name']).extract()

            if not item['name']:
                item['name'] = sel.xpath(
                    xpaths['name'].replace('/text()', '/a/text()')
                ).extract()
                
            # MMKB pages don't mention the chip element pre-MMBN4 :/
            if self.game in ('bn4', 'bn5', 'bn6'):
                item['element'] = sel.xpath(xpaths['element']).extract()
            else:
                item['element'] = ''

            if xpaths['size']:
                item['size'] = sel.xpath(xpaths['size']).extract()
            else:
                item['size'] = ''

            if xpaths['codes']:
                item['codes'] = sel.xpath(xpaths['codes']).extract()
            else:
                item['codes'] = ''

            if self.classification:
                item['classification'] = self.classification
            else:
                item['classification'] = 'standard'

            item['power'] = sel.xpath(xpaths['power']).extract()
            item['stars'] = ''

            # Hacky solution to missing attributes, but it shall do.
            if self.game == 'bn1':
                key = item['indice'][0].lstrip('0')
                item['element'] = _bn1_attrs[key][0]
                item['stars'] = _bn1_attrs[key][1]
                item['codes'] = _bn1_attrs[key][2]
            # Spit it all out!
            yield item
