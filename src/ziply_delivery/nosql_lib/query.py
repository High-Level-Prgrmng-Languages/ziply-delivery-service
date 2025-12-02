class QueryBuilder:
    def __init__(self, collection):
        self.collection = collection
        self._filters = {}
        self._sort = []
    
    def filter(self, **kwargs):
        self._filters.update(kwargs)
        return self
    
    def sort(self, field: str, direction: int = 1):
        self._sort.append((field, direction))
        return self
    
    def execute(self):
        cursor = self.collection.find(self._filters)
        if self._sort:
            cursor = cursor.sort(self._sort)
        return list(cursor)