## Django imports
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect

## Python imports
import json
import requests

def createJSONResponse(data):
    response_data = { "success" : True, "data" : data }
    return HttpResponse(content=json.dumps(response_data), content_type="application/json")


# Create your views here.
def index(request):
    #return createJSONResponse({})
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def search(request):
    query = request.GET.get("query")
    
    if (query is None or query == ""):
        return index(request)
    
    job_response = requests.get("http://api.usa.gov/jobs/search.json?query=" + query)
    response_data = job_response.json()
    
    #return createJSONResponse(job_response.json())
    return render(request, "search.html", { "data": job_response.json(), "query": query })