from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import author,article,category

# Create your views here.


def index(request):

    post=article.objects.all()
    context={
        "post":post
    }
    return render(request,"index.html",context)

def getauthor(request, name):

    return  render(request, "profile.html")

def getsingle(request, id):
    post=get_object_or_404(article, pk=id)
    first=article.objects.first()
    last=article.objects.last()
    related=article.objects.filter(category=post.category).exclude(id=id)[:4]
    context={
        "post":post,
        "first":first,
        "last":last,
        "related":related

    }

    return  render(request, "single.html",context)

def gettopic(request, name):
    cat=get_object_or_404(category,name=name)
    post=article.objects.filter(category=cat.id)

    return  render(request, "category.html",{"post":post,"cat":cat})
