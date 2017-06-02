from django.http import HttpResponse
from django.template.loader import get_template
from service.user import *

def users(request):

	
	create_user({'Name':'thiago',
	             'Avatar':'abc',
	             'JoinDate':'21/05/2017',
	             'LastSeen':'21/05/2017',
	             'Location':'Brasil',
	             'Friends':[''],
	             'NumberFriended':'1',
	             'Files':[''],
	             'Packs':[''],
	             'Scripts':[''],
	             'Credited':'5',
	             'Rating':'4.4',
	             'Description': 'TEXTO DESCREVENDO O USER',
	             'OtherDetails': 'blé',
	             'Interests':'Nenhum',
	             'Fieldindustry':'Medical',
	             'Occupationroles':'Doctor',
	             'Organisations':'UFF'})
	
	#create_user({'name':"thiago",'avatar':'imagem','JoinDate':,'LastSeen':,'Email':,'website':,'Location':,'Frieds':,'NumberFriended':,'Groups':,'Files':,'Packs':,'Scripts':,'Credited':,'Rating':,'Description':,'OtherDetails':,'Interests':,'Field/industry':,'Occupation/roles':,'Organisations':})
	mostFriend = get_user_mostFriends()
	mostCredited = get_users_credited()
	highRated = get_users_rating()
	params = {'friend': mostFriend,'credited': mostCredited,'rated': highRated}
	t = get_template("users.html")
	html = t.render(dict(params))
	return HttpResponse(html)
