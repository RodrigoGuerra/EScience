from bson.objectid import ObjectId
from pymongo.collection import ReturnDocument

from libs.mongo import *


def get_groups():
    groups = []
    for group in db.groups.find({}):
        stringify_id(group)
        groups.append(group)
    return groups


def get_groups_sharedItems():
    groups = []
    for group in db.groups.find({}).sort('SharedItems', -1).limit(10):
        stringify_id(group)
        groups.append(group)
    return groups


def get_groups_credited():
    groups = []
    for group in db.groups.find({}).sort('CreditedBy', -1).limit(10):
        stringify_id(group)
        groups.append(group)
    return groups


def get_groups_mostMembers():
    groups = []
    for group in db.groups.find({}).sort('Members', -1).limit(10):
        stringify_id(group)
        groups.append(group)
    return groups


def get_groups_mostRecent():
    groups = []
    for group in db.groups.find({}).sort('CreatedAt', -1).limit(10):
        stringify_id(group)
        groups.append(group)
    return groups


def create_group(user):
    db.groups.insert_one(user)
    stringify_id(user)
    return ObjectId


def update_group(id, group):
    new_group = db.groups.find_one_and_update({'_id': ObjectId(id)}, {'$set': group},return_document=ReturnDocument.AFTER)
    stringify_id(new_group)
    return new_group

def get_group(id):
    new_group = db.groups.find_one({'_id': ObjectId(id)})
    stringify_id(new_group)
    return new_group

def delete_group(id):
    return db.groups.find_one_and_delete({'_id': ObjectId(id)})
