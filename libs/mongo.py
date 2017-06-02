from pymongo import MongoClient
import gridfs

db = MongoClient('mongodb://127.0.0.1:27017/')["e-sci"]
fs = gridfs.GridFS(db)

def stringify_id(element):
    if element is not None:
        element['_id'] = str(element['_id'])
