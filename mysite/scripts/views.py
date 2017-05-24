from django.http import HttpResponse
from django.template.loader import get_template
from service.script import *

def scripts(request):
	script={
	'Authors':[{'name':'Thiago'}],
	'Title':'Script1',
	'Uploader':'Thiago',
	'License':'FREE',
	'Description':'ASDHUASDAHSDASKDJASDLKAHSDKJASDJKAHSD',
	'Version':'1.0',
	'createdOn':'23/05/2017',
	'lastEdited':'23/05/2017',
	'Credits':[{'Name':'Thiago'}],
	'Attribuitions':'',
	'Tags':[{'name':'BOA'},{'nae':'ruim'}],
	'SharedGroups':[{'name':'nome'}],
	'FeaturedPacks':'',
	'FavouritedBy':'',
	'Views':4842,
	'Downloads':4451,
	'Inputs':'ABC',
	'Outputs':"DFG",
	'Citations':'SOW CUTES',
	'Reviews':'VERY GOOD',
	'Comments':'blabla',
	'PyVersion':'2,7'
	
	}
	
	create_script(script);
	scripts = get_scripts()
	
	t = get_template("scripts.html")
	html = t.render(dict({'scripts': scripts}))
	return HttpResponse(html)
