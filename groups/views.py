from django.http import HttpResponse
from django.template.loader import get_template

from service.groups import *


def groups(request):
    create_group({
        'Owner': 'thiago',
        'News': 'Novidades do grupo!!',
        'Members  ': [{'Name': 'rodrigo'}, {'Name': 'leonardo'}],
        'Description': 'escience',
        'SharedItems': '5',
        'Announcements': 'trabalho',
        'Tags': [{'Name': 'escience'}, {'Name': 'scripts'}],
        'CreatedAt': '23/03/2017',
        'UniqueName': 'Grupo de trabalho',
        'CreditedBy': 'rlt'})

    mostRecent = get_groups_mostRecent()
    mostMembers = get_groups_mostMembers()
    mostShared = get_groups_sharedItems()
    mostCredited = get_groups_credited()
    t = get_template("groups.html")
    html = t.render(
        dict({'groupsMR': mostRecent, 'groupsMM': mostMembers, 'groupsMS': mostShared, 'groupsMC': mostCredited}))
    return HttpResponse(html)

def newGroup(request):
    t = get_template("newGroup.html")
    html = t.render(
        dict({}))
    return HttpResponse(html)

def groupDetails(request, group_id):
    group = get_group(group_id)
    t = get_template("groupDetails.html")
    html = t.render(dict({'group': group}))
    return HttpResponse(html)