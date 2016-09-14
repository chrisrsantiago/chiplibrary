# -*- coding: utf-8 -*-
import os
import shutil

import whoosh
import whoosh.fields
import whoosh.index
from whoosh import writing, scoring
from whoosh.qparser import MultifieldParser
from whoosh.filedb.filestore import FileStorage
from pyramid.settings import asbool

from ..db import Chip


class FuzzyTerm(whoosh.query.FuzzyTerm):
     def __init__(self,
        fieldname,
        text,
        boost=1.0,
        maxdist=4,
        prefixlength=2,
        constantscore=True
    ):
         super(FuzzyTerm, self).__init__(
            fieldname,
            text,
            boost,
            maxdist,
            prefixlength, 
            constantscore
        )

class ChipSchema(whoosh.fields.SchemaClass):
    id = whoosh.fields.ID(sortable=True, stored=True)
    indice = whoosh.fields.ID(sortable=True, stored=True)
    name = whoosh.fields.ID
    name_display = whoosh.fields.ID(sortable=True, stored=True)
    game = whoosh.fields.ID(sortable=True, stored=True)
    game_enum = whoosh.fields.STORED
    version = whoosh.fields.ID(sortable=True, stored=True)
    version_enum = whoosh.fields.STORED
    classification = whoosh.fields.ID(sortable=True, stored=True)
    classification_enum = whoosh.fields.STORED
    element = whoosh.fields.ID(sortable=True, stored=True)
    element_enum = whoosh.fields.STORED
    description = whoosh.fields.STORED
    codes = whoosh.fields.KEYWORD(sortable=True, commas=True)

class Library(object):

    RESULTS_LIMIT = 50
    SUGGESTIONS_LIMIT = 5
    
    def __init__(self, dbsession, **settings):
        """Initializes Whoosh by setting up and loading indexes for lookup."""
        self._dbsession = dbsession
        self.schema = ChipSchema()
        self.directory = settings.get(
            'whoosh.store',
            os.path.join(settings['config_path'], 'whoosh-data')
        )
        self.indexname = settings.get(
            'whoosh.indexname',
            'chips'
        )
        self.rebuild = asbool(settings.get('whoosh.rebuild', 'false'))
        self.storage = FileStorage(self.directory)

        self.setindex()
        
        if self.rebuild:
            self.buildindex()

    def setindex(self):
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)

        if whoosh.index.exists_in(
            self.directory,
            indexname=self.indexname
        ):
            if self.rebuild:
                shutil.rmtree(self.directory)
                self.setindex()
            else:
                self.index = self.storage.open_index(indexname=self.indexname)
        else:
            self.index = self.storage.create_index(
                self.schema,
                indexname=self.indexname
            )
            
    def buildindex(self):
        q = self._dbsession.query(Chip).all()
        writer = self.index.writer()
        for chip in q:
            try:
                version = chip.version.name
            except AttributeError:
                version = ''

            writer.add_document(
                id=str(chip.id),
                indice=str(chip.indice),
                name=chip.name.lower(),
                name_display=chip.name,
                game=chip.game.name.lower(),
                game_enum=chip.game,
                version=version,
                version_enum=chip.version,
                classification=chip.classification.name,
                classification_enum=chip.classification,
                element=chip.element.name,
                element_enum=chip.element,
                description=chip.description,
                codes=u','.join(chip.codes_iter()).lower()
            )
        writer.commit(writing.CLEAR)
        
    def lookup(self, term, prefix=False, limit=None):
        term = term.lower()

        if limit:
            limit = limit
        else:
            if prefix:
                limit = self.SUGGESTIONS_LIMIT
            else:
                limit = self.RESULTS_LIMIT

        if prefix:
            query = whoosh.query.Prefix('name', term)
        else:
            parser = MultifieldParser(
                [
                    'name',
                    'game',
                    'version',
                    'classification',
                    'element',
                    'codes'
                ],
                schema=self.index.schema,
                termclass=FuzzyTerm
            )
            query = parser.parse(term)
            
        searcher = self.index.searcher()
        results = searcher.search(query, limit=limit)

        return results
        
def includeme(config):
    settings = config.get_settings()
    library = Library(config.registry['dbsession_factory'](), **settings)
    
    config.add_request_method(
        # r.tm is the transaction manager used by pyramid_tm
        lambda l: library,
        'library',
        reify=True
    )
