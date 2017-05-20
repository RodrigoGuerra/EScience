from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def users(request):
	t = get_template("users.html")
	html = t.render(dict())
	return HttpResponse(html)