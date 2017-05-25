from django.http import HttpResponse
from django.template.loader import get_template
from service.groups import *

def groups(request):
	mostRecent  = get_groups_mostRecent()
	mostMembers = get_groups_mostMembers()
	mostShared = get_groups_sharedItems()
	mostCredited = get_groups_credited()
	t = get_template("groups.html")
	html = t.render(dict({'groupsMR':mostRecent,'groupsMM':mostMembers, 'groupsMS':mostShared,'groupsMC':mostCredited}))
	return HttpResponse(html)
