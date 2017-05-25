from django.http import HttpResponse
from django.template.loader import get_template
from service.groups import *

def groups(request):
	create_group({
				'Owner': 'thiago',
	              'News': 'abc',
	              'Members  ':[ {'Name': 'rodrigo'}, {'Name': 'leonardo'}],
	              'Description': 'escience',
	              'SharedItems': '5',
	              'announcements': 'trabalho',
	              'Tags': [{'Name':'escience'},{'Name':'scripts'}],
	              'CreatedAt': 'abc',
	              'UniqueName': 'Grupo Bolado',
	              'CreditedBy': 'rlt'})
	
	mostRecent  = get_groups_mostRecent()
	mostMembers = get_groups_mostMembers()
	mostShared = get_groups_sharedItems()
	mostCredited = get_groups_credited()
	t = get_template("groups.html")
	html = t.render(dict({'groupsMR':mostRecent,'groupsMM':mostMembers, 'groupsMS':mostShared,'groupsMC':mostCredited}))
	return HttpResponse(html)
