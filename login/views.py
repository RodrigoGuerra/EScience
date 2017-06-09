from django.http import HttpResponse
from django.template.loader import get_template

def logins(request):
    params = {}
    t = get_template("login.html")
    html = t.render(dict(params))
    return HttpResponse(html)
