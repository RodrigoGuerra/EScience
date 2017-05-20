from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def scripts(request):
	t = get_template("scripts.html")
	html = t.render(dict())
	return HttpResponse(html)