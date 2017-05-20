from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def files(request):
	t = get_template("files.html")
	html = t.render(dict())
	return HttpResponse(html)