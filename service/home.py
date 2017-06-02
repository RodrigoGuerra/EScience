from libs.mongo import *
from pymongo.collection import ReturnDocument
from bson.objectid import ObjectId

def get_recent_packs():
    packs =[]
    for pack in db.pack.find({}).sort('LastEdited',-1).limit(10):
        stringify_id(pack)
        packs.append(pack)
    return packs

def get_recent_files():
    files =[]
    for file in db.files.find({}).sort('lastEdited',-1).limit(10):
        stringify_id(file)
        files.append(file)
    return files

def get_recent_scripts():
    scripts = []
    for script in db.script.find({}).sort('lastEdited',-1).limit(10):
        stringify_id(script)
        scripts.append(script)
    return scripts