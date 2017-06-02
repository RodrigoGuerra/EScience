from bson.objectid import ObjectId
from pymongo.collection import ReturnDocument

from libs.mongo import db, stringify_id


def get_users():
    users = []
    for user in db.users.find({}):
        stringify_id(user)
        users.append(user)
    return users


def create_user(user):
    db.users.insert_one(user)
    stringify_id(user)
    return ObjectId


def update_user(id, user):
    new_user = db.users.find_one_and_update({'_id': ObjectId(id)}, {'$set': user}, return_document=ReturnDocument.AFTER)
    stringify_id(new_user)
    return new_user


def delete_user(id):
    return db.users.find_one_and_delete({'_id': ObjectId(id)})
