from pymongo import MongoClient

db = MongoClient('mongodb://127.0.0.1:27017/')["e-sci"]

def stringify_id(element):
    if element is not None:
        element['_id'] = str(element['_id'])
