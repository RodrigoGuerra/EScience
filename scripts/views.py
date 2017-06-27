from django.http import HttpResponse
from django.template.loader import get_template

from service.script import *


def scripts(request):
    script = {
        'Authors': [{'Name': 'Thiago'}],
        'Title': 'Script1',
        'Uploader': 'Thiago',
        'License': 'FREE',
        'Description': 'Descrição  do script para apresentação',
        'Version': '1.0',
        'CreatedOn': '23/05/2017',
        'LastEdited': '23/05/2017',
        'Credits': [{'Name': 'Thiago'}],
        'Attribuitions': '',
        'Tags': [{'Name': 'TAG4'}, {'Namw': 'Tag1'}],
        'SharedGroups': [{'Name': 'nome'}],
        'FeaturedPacks': '',
        'FavouritedBy': '',
        'Views': 4842,
        'Downloads': 4451,
        'Inputs': 'In1',
        'Outputs': "Out2",
        'Citations': 'Alguma citação',
        'Reviews': 'Review positiva sobre o script',
        'Comments': 'Comentario sobre o script',
        'PyVersion': '2,7'

    }

    create_script(script);
    scripts = get_scripts()

    t = get_template("scripts.html")
    html = t.render(dict({'scripts': scripts}))
    return HttpResponse(html)

def newScript(request):
    t = get_template("Newscript.html")
    html = t.render(dict({}))
    return HttpResponse(html)
