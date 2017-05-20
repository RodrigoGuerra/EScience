from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def groups(request):
	t = get_template("groups.html")
	html = t.render(dict())
	return HttpResponse(html)