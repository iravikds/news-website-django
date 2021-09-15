from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer
import requests


# Create your views here.
def home(request):
    search_term = ''

    if 'search' in request.GET:
        search_term = request.GET['search']
        news = News.objects.all().filter(title__icontains=search_term).order_by('-created')
    else:
        r = requests.get('http://127.0.0.1:8000/api')
        news = r.json()
    return render(request, "home.html", {'news': news, 'search_term': search_term})
    
    
@api_view(['GET'])
def news_list(request):
    if request.method == 'GET':
        posts = News.objects.order_by('-created')
        serializer = NewsSerializer(posts, many=True)
        return Response(serializer.data)