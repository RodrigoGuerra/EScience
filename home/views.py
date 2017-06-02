from django.http import HttpResponse
from django.template.loader import get_template
from service.user import *
from service.home import *
from service.script import *
from service.pack import *
from service.files import *
from service.groups import *

from libs.mongo import db, stringify_id
from pymongo.collection import ReturnDocument
from bson.objectid import ObjectId



def home(request):
	file = get_recent_files()
	packs = get_recent_packs()
	scripts = get_recent_scripts()
	
	all_lists = sum([file, packs, scripts], [])
	list = []
	list = list + file
	list = list + packs
	list = list + scripts
	
	user = get_users()
	pack = get_packs()
	script = get_scripts()
	file = get_files()
	group = get_groups()
	parametros = {"users": user,'packs':pack,'scripts':script,'groups':group,'files':file,"activity":all_lists}
	t = get_template("home.html")
	html = t.render(dict(parametros))
	return HttpResponse(html)
