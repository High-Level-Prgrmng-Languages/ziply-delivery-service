from pymongo import MongoClient
from typing import Dict, Any, List, Optional

class NoSQLClient:
    def __init__(self, connection_string: str, database_name: str):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
    
    def create_collection(self, name: str) -> 'Collection':
        return Collection(self.db[name])
    
    def get_collection(self, name: str) -> 'Collection':
        return Collection(self.db[name])