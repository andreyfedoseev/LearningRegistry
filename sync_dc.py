#!/usr/bin/env python
import couchdb, sys
from oaipmh.client import Client
from oaipmh.common import Identify, Metadata, Header
from oaipmh.metadata import MetadataRegistry, oai_dc_reader , MetadataReader
from util import *
def format(doc):
    if not ''.join(doc.getField('identifier')).startswith('fedora'):
        value = {'title':''.join(doc.getField('title')),'identifier':''.join(doc.getField('identifier')), 'location': ''}
        return value
if __name__ == '__main__':
    main_url = 'http://wegrata:g15t15@wegrata.couchone.com'    
    oai_url  = 'http://localhost:8080/fedora/oai'
    database_name = 'learningregistry2'
    index_documents(oai_url,main_url,database_name,oai_dc_reader,'oai_dc', format)