from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def packs(request):
	t = get_template("packs.html")
	html = t.render(dict())
	return HttpResponse(html)