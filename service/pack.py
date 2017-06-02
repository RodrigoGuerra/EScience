from libs.mongo import db, stringify_id
from pymongo.collection import ReturnDocument
from bson.objectid import ObjectId
import pymongo

def get_packs():
    packs = []
    for pack in db.pack.find({}):
        stringify_id(pack)
        packs.append(pack)
    return packs

def create_pack(pack):
    db.pack.insert_one(pack)
    stringify_id(pack)
    return ObjectId

def update_pack(id, pack):
    new_pack = db.pack.find_one_and_update({'_id': ObjectId(id)}, {'$set': pack}, return_document=ReturnDocument.AFTER)
    stringify_id(new_pack)
    return new_pack

def delete_pack(id):
    return db.pack.find_one_and_delete({'_id': ObjectId(id)})
