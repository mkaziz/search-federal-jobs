## Django imports
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect

## Python imports
import json

def createJSONResponse(data):
    response_data = { "success" : True, "data" : data }
    return HttpResponse(content=json.dumps(response_data), content_type="application/json")


# Create your views here.
def index(request):
    return createJSONResponse({})
    #return render(request, "index.html")