from django.http import HttpResponse
from django.template.loader import get_template
from service.pack import *

def packs(request):
	pack={
	'Title':'Pacote com arquivos testes',
	'Creator': 'joao goulard',
	'Description':'pacote com varios arquiovs bolados para uso cauteloso',
	'Tags':[{'Name':'blabla'}],
	'SharedGroups':[{'Name': 'pasta'}],
	'FeaturedPacks':'wer',
	'FavouriteBy':487,
	'CreatedOn':'23/43/65',
	'LastEdited':'12/5476/76',
	'Views':3434,
	'Downloads':345,
	'Comments':'werwer',
	'Items': [{'Name': 'arquivo'}, {'Name': 'arquivo'}, {'Name': 'arquivo'}, {'Name': 'arquivo'}]
	
	}
	create_pack(pack)
	p = get_packs()
	t = get_template("packs.html")
	html = t.render(dict({'packs': p}))
	return HttpResponse(html)