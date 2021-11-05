from django.shortcuts import render
from .models import HomePageData


# Create your views here.
def index(req):
    homePageData = HomePageData.objects.all()[0]
    context = {'data': homePageData}
    return render(req, 'blog/index.html', context)

def posts(req):
    return render(req, 'blog/posts.html')