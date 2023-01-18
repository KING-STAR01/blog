from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import Article, Comments, UserProfile

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, PasswordChangeForm
from django.contrib.auth import authenticate, login as loggin, logout
from django.core.mail import send_mail

def home(request):
    posts = Article.objects.all()
    context = {"articles" : posts}
    print(settings.MEDIA_ROOT)
    return render(request, 'blog/home.html', context=context)

def detailView(request, slug):
    post = Article.objects.get(slug=slug)
    print(post)
    context = {"post":post}
    return render(request, 'blog/detail.html', context=context)

def login(request):
    if request.method == "GET":
        fm = AuthenticationForm()
        context = {"form":fm}
        return render(request, 'blog/login.html', context=context)
    else:
        fm = AuthenticationForm(data = request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(username=username,password=password)
            print(user, "is authenticated")
            loggin(request,user)
            return redirect('home')
        else:
            context = {"form":fm}
            return render(request, 'blog/login.html', context=context)

def signup(request):
    if request.method == "GET":
        fm = UserCreationForm()
        context = {"form":fm}
        return render(request, "blog/register.html", context=context)
    else:
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            print(fm)
            user = fm.save()
            if user is not None:
                return redirect('login')
            else:
                context={"form":fm}
                return render(request,'blog/register.html', context=context)

@login_required(login_url='login')
def signout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def send_mails(request,*args):
    send_mail('hello testing mail','iam going to be the message body', 'cprasanth4321@gmail.com',['prasanth@stockone.com'])
    return HttpResponse("mail sent successfully.")

def getCategory(request, cat):
    print("getting correctly")
    articlelist = Article.objects.filter(category=cat)
    print(articlelist)
    context = {"articles" : articlelist, "category":cat}
    return render(request, 'blog/category.html',context=context)

            