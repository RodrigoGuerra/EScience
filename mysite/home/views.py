from django.http import HttpResponse
from django.template.loader import get_template
from service.user import *

from libs.mongo import db, stringify_id
from pymongo.collection import ReturnDocument
from bson.objectid import ObjectId



def home(request):
	id = create_user({'nome': "Thiago Cordeiro",'idade': 25})
	users = get_users()
	parametros = {"users": users}
	t = get_template("home.html")
	html = t.render(dict(parametros))
	return HttpResponse(html)
