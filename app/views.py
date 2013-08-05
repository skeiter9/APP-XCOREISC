from django.shortcuts  import render_to_response
from app.models import *
from django.template import RequestContext

def home(request):
	return render_to_response('home.html',RequestContext(request))

def index(request):
	return render_to_response('index.html',RequestContext(request))

def pages(request, pk):
    event = Events.objects.get(pk=int(pk))
    last = Events.objects.order_by('-envio')[:5]
    d = dict(event=event, last=last)
    return render_to_response("pages.html", d, RequestContext(request))