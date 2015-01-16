from django.shortcuts import render
from django.http.response import HttpResponse
from django.template import RequestContext, loader

def homepage(request):
    context = RequestContext(request, {'title': 'Dungeons and Dragons'})
    template = loader.get_template("chargen/homepage.html")
    return HttpResponse(template.render(context))
