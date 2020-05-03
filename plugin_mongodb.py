#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bson.objectid import ObjectId
from deepnlpf.helpers.mongodb import ConnectMongoDB

from deepnlpf.iplugindb import IPluginDB

class Plugin(IPluginDB):
    
    def __init__(self):
        self.db = ConnectMongoDB()
        self.collection = ['dataset', 'document', 'analysi', 'log']

    def insert(self, collection, document):
        db_response = self.db.insert_document(collection, document)
        return db_response

    def select_one(self, collection, key):
        db_response = self.db.select_document(collection, key)
        return db_response

    def select_all(self, collection):
        db_response = self.db.select_document_all(collection)
        return db_response

    def select_all_key(self, collection, key):
        db_response = self.db.select_document_all_key(collection, key)
        return db_response

    def update(self, collection, key, document):
        db_response = self.db.update(collection, key, document)
        return db_response

    def delete(self, collection, key):
        db_response = self.db.delete(collection, key)

        if db_response.deleted_count:
            return True
        else:
            return False