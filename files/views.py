import json

from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template

from service.files import *


def files(request):
    file = {
        'Title': 'Arquivo',
        'Version': '1.0',
        'CreatedOn': '22/05/2017',
        'LastEdited': '22/05/2017',
        'FileName': 'Aqruivo Teste',
        'Filesize': '3054',
        'ContentType': 'Arquivo de Scripts',
        'Description': 'Arquivo teste de scripts',
        'Uploader': 'Thiago',
        'License': 'free',
        'Credits': 'none',
        'Attributions': 'idk',
        'Tags': [{'Name': 'TAG1'}, {'Name': 'TAG2'}],
        'Type': 'file',
        'SharedGroups': [{'Groupname': 'UFF'}],
        'FeaturedInPacks': [{'Name': 'Pack1'}, {'Name': 'Pack2'}],
        'AttibutedBy': 325,
        'FavouritedBy': 245,
        'Downloads': 450,
        'Views': 9875,
        'Comments': {'Comment': 'Comentario sobre o arquivo'}}
    create_file(file)

    fil = get_files()
    t = get_template("files.html")
    html = t.render(dict({'files': fil}))
    return HttpResponse(html)


def newFile(request):
    t = get_template("newFile.html")
    html = t.render(dict({}))
    return HttpResponse(html)


def fileDetails(request, file_id):
    f = get_file(file_id)

    t = get_template("fileDetails.html")
    html = t.render(dict({'file': f}))
    return HttpResponse(html)


def insertFile(request):
    if (request.method == "POST"):
        file = json.loads(request.body.decode("utf-8"))
        res = create_file(file)
        return JsonResponse(res, status=201)
    else:
        response_data = {
            "result": "error",
            "message": "Invalid method",
        }
        return JsonResponse(response_data, status=405)
