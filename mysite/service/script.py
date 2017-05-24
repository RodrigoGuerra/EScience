from libs.mongo import db, stringify_id
from pymongo.collection import ReturnDocument
from bson.objectid import ObjectId
import pymongo

def get_scripts():
    scripts = []
    for script in db.script.find({}):
        stringify_id(script)
        scripts.append(script)
    return scripts


def create_script(script):
    db.script.insert_one(script)
    stringify_id(script)
    return ObjectId

def update_file(id, script):
    new_script = db.script.find_one_and_update({'_id': ObjectId(id)}, {'$set': script}, return_document=ReturnDocument.AFTER)
    stringify_id(new_script)
    return new_script

def delete_user(id):
    return db.script.find_one_and_delete({'_id': ObjectId(id)})
