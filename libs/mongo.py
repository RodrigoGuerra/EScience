import os
import gridfs
from pymongo import MongoClient

db = MongoClient(os.environ['MONGODB_CONNECTION_STRING'])["e-sci"]
fs = gridfs.GridFS(db)


def stringify_id(element):
    if element is not None:
        element['_id'] = str(element['_id'])
