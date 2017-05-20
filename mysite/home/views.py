from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def home(request):
	t = get_template("home.html")
	titulo1 = {'titulo': 'Myscripts'}
	html = t.render(dict(titulo1))
	return HttpResponse(html)