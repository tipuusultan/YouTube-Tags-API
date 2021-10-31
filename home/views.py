from django.shortcuts import render, HttpResponse
import json
from YoutubeTags import videotags


# Create your views here.

def home(request):
    return HttpResponse("<h1>Unofficial Youtube Tag Extract API</h1>")

def get_data(request):
    url = request.GET.get('url', '')

    tags = videotags(url)

    json_data = {
        'tags':tags
    }

    return HttpResponse(json.dumps(json_data),content_type="application/json")