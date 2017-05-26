from django.http import HttpResponse
from django.template.loader import get_template
from service.files import *

def files(request):
	file = {
	'Title':'Arquivo',
	'version':'1.0',
	'createdOn':'22/05/2017',
	'lastEdited':'22/05/2017',
	'FileName':'Aqruivo Teste',
	'filesize':'3054',
	'ContentType':'Arquivo de Scripts',
	'Description':'Arquivo teste de scripts',
	'Uploader':'Thiago',
	'License':'free',
	'Credits':'none',
	'Attributions':'idk',
	'Tags':[{'Name':'TAG1'},{'Name':'TAG2'}],
	'Type':'file',
	'SharedGroups':[{'Groupname':'UFF'}],
	'FeaturedInPacks':'',
	'AttibutedBy':325,
	'FavouritedBy':245,
	'Downloads':450,
	'Views':9875,
	'Comments':{'Comment':'Comentario sobre o arquivo'}}
	create_file(file)
	
	fil = get_files()
	t = get_template("files.html")
	html = t.render(dict({'files': fil}))
	return HttpResponse(html)