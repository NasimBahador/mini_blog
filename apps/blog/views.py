from django.shortcuts import render, HttpResponse, redirect
from models import Post

# Create your views here.
def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/index.html", context)

def login(request):
    pass

def post(request):
    Post.postMgr.add(request.POST)
    
