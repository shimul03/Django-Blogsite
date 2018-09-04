from django.shortcuts import render, HttpResponse, get_object_or_404,redirect
from .models import author,article,category
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.


def index(request):

    post=article.objects.all()
    context={
        "post":post
    }
    return render(request,"index.html",context)

def getauthor(request, name):
    post_author=get_object_or_404(User, username=name)
    auth=get_object_or_404(author, name=post_author.id)
    post=article.objects.filter(article_author=auth.id)
    context={
        "auth":auth,
        "post":post
    }

    return  render(request, "profile.html",context)

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

def getlogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('index')


    return render(request,"login.html")
def getlogout (request):
    logout(request)
    return redirect('index')

