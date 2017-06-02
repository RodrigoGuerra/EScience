from bson.objectid import ObjectId
from pymongo.collection import ReturnDocument

from libs.mongo import *


def get_users():
    users = []
    for user in db.users.find({}):
        stringify_id(user)
        users.append(user)
    return users


def get_users_rating():
    users = []
    for user in db.users.find({}).sort('credited', -1).limit(10):
        stringify_id(user)
        users.append(user)
    return users


def get_users_credited():
    users = []
    for user in db.users.find({}).sort('rating', -1).limit(10):
        stringify_id(user)
        users.append(user)
    return users


def get_user_mostFriends():
    users = []
    for user in db.users.find({}).sort('NumberFriended', -1).limit(10):
        stringify_id(user)
        users.append(user)
    return users


def create_file(file):
    fs.put(file)
    stringify_id(file)
    return ObjectId


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
