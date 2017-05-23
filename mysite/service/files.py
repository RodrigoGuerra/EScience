from libs.mongo import db, stringify_id
from pymongo.collection import ReturnDocument
from bson.objectid import ObjectId
import pymongo

def get_files():
    files = []
    for file in db.files.find({}):
        stringify_id(file)
        files.append(file)
    return files


def create_file(files):
    db.files.insert_one(files)
    stringify_id(files)
    return ObjectId

def update_file(id, file):
    new_file = db.files.find_one_and_update({'_id': ObjectId(id)}, {'$set': file}, return_document=ReturnDocument.AFTER)
    stringify_id(new_file)
    return new_file

def delete_user(id):
    return db.files.find_one_and_delete({'_id': ObjectId(id)})
