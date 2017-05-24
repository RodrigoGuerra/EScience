from django.http import HttpResponse
from django.template.loader import get_template
from service.files import *

def files(request):
	file = {
	'Title':'arquivo',
	'version':'1.0',
	'createdOn':'22/05/2017',
	'lastEdited':'22/05/2017',
	'FileName':'AqruivoTeste',
	'filesize':'3054',
	'ContentType':'Arquivo de Scripts',
	'Description':'Arquivo teste de scripts',
	'Uploader':'Thiago',
	'License':'free',
	'Credits':'none',
	'Attributions':'idk',
	'Tags':[{'name':'sds'},{'name':'sdd'}],
	'Type':'file',
	'SharedGroups':[{'groupname':'abestados'}],
	'FeaturedInPacks':'',
	'AttibutedBy':325,
	'FavouritedBy':245,
	'Downloads':450,
	'Views':9875,
	'Comments':{'comment':'VERY GOLD'}}
	create_file(file)
	
	fil = get_files()
	t = get_template("files.html")
	html = t.render(dict({'files': fil}))
	return HttpResponse(html)