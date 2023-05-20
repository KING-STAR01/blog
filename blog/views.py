from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages # this is used for displaying messages

from .models import Article, Comments, UserProfile
from .forms import ArticleForm, CommentsForm, UserProfileForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, PasswordChangeForm
from django.contrib.auth import authenticate, login as loggin, logout
from django.core.mail import send_mail

def home(request):
    posts = Article.objects.filter(active = True)
    context = {"articles" : posts}
    if request.user.is_authenticated:
        context["profile"] = UserProfile.objects.prefetch_related('favourite','read_later').get(pk=request.user.id)
    print(settings.MEDIA_ROOT)
    return render(request, 'blog/home.html', context=context)



def detailView(request, slug):
    post = Article.objects.get(slug=slug)
    comments = post.comments.prefetch_related('user').filter(active = True)
    comments_form = CommentsForm()
    # print(comments)
    # print(post)
    context = {"post":post, "comments":comments, "comment_form":comments_form}
    if request.user.is_authenticated:
        context["profile"] = UserProfile.objects.prefetch_related('favourite','read_later').get(pk=request.user.id)
    return render(request, 'blog/detail.html', context=context)



@login_required(login_url='login')
def add_comment(request, slug):
    post = Article.objects.get(slug=slug)

    if request.method == 'GET':
        # add error message to display type of error
        print('hello')
        return redirect('detail',slug)
    comment = CommentsForm(data=request.POST)
    if comment.is_valid():
        comment = comment.save(commit=False)
        comment.user = request.user
        comment.article = post
        comment.save()
    return redirect('detail', slug)



def login(request):
    if request.method == "GET":
        fm = AuthenticationForm()
        context = {"form":fm}
        print('iam from get')
        return render(request, 'blog/login1.html', context=context)
    else:
        print('iam from post')

        fm = AuthenticationForm(data = request.POST)
        print(request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(username=username,password=password)
            print(user, "is authenticated")
            loggin(request,user)
            return redirect('home')
        else:
            context = {"form":fm}
            return render(request, 'blog/login1.html', context=context)



def signup(request):
    if request.method == "GET":
        fm = UserCreationForm()
        context = {"form":fm}
        return render(request, "blog/register1.html", context=context)
    else:
        print(request.POST)
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            print(fm)
            user = fm.save()
            if user is not None:
                return redirect('login')
            else:
                context={"form":fm}
                return render(request,'blog/register1.html', context=context)
        else:
            fm = UserCreationForm()
            context = {"form":fm}
            return render(request, "blog/register1.html", context=context, status=401)




@login_required(login_url='login')
def signout(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    #return redirect('home')



@login_required(login_url='login')
def send_mails(request,**kwargs):
    send_mail(kwargs['heading'], kwargs['body'], kwargs['email'], ['prasanth@stockone.com'])
    return HttpResponse("mail sent successfully.")



def getCategory(request, cat):
    print("getting correctly")
    articlelist = Article.objects.filter(category=cat.upper(), active = True)
    print(articlelist)
    context = {"articles" : articlelist, "category":cat}
    if request.user.is_authenticated:
        context["profile"] = UserProfile.objects.prefetch_related('favourite', 'read_later').get(pk=request.user.id)
    return render(request, 'blog/category.html',context=context)

@login_required(login_url='login')
def go_to_type(request, type):
    user = request.user
    profile = UserProfile.objects.prefetch_related('favourite','read_later').get(user = user)
    if 'fav' in type.lower():
        articlelist = profile.favourite.all()
    elif 'my posts' in type.lower():
        articlelist = Article.objects.filter(author = user)
    else:
        articlelist = profile.read_later.all()
    print(articlelist)
    context = {"articles" : articlelist, "category": type}
    context["profile"] = profile
    return render(request, 'blog/category.html',context=context)




@login_required(login_url='login')
def write(request):
    if request.method == "GET":
        fm = ArticleForm()
        context = {'fm':fm}
        context['profile'] = UserProfile.objects.get(user = request.user)
        return render(request, 'blog/create.html', context=context)
    else:
        print(request.POST)
        fm = ArticleForm(request.POST, request.FILES)
        context = {'fm':fm}
        if fm.is_valid():
            post = fm.save(commit=False)
            print(post.image)
            post.author = request.user
            #remove below comment to make post visible only after review
            # post.active = False
            post.save()
            send_mails(request, heading = 'hey hi you got new post to approve', body = str(request.user) + " wrote a new post in " + str(post.category) + ' he is waiting for your approval', email = 'cprasanth4321@gmail.com')
            #return HttpResponse('labe when admin approves it')
            messages.info(request, 'Your Post will be available once admin approves it')
            return redirect('home')
            # need to update
        else:
            return render(request, 'blog/create.html', context=context)




@login_required(login_url='login')
def add_to_fav(request,slug):
    auth_user = request.user
    post = Article.objects.get(slug=slug)
    profile = UserProfile.objects.get(user = auth_user)
    if profile.favourite.contains(post):
        profile.favourite.remove(post)
    else:
        profile.favourite.add(post)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return HttpResponseRedirect("")



@login_required(login_url='login')
def add_to_readlater(request, slug):
    auth_user = request.user
    post = Article.objects.get(slug = slug)
    profile = UserProfile.objects.get(user = auth_user)
    if profile.read_later.contains(post):
        profile.read_later.remove(post)
    else:
        profile.read_later.add(post)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return HttpResponseRedirect("")


@login_required(login_url='login')
def profile(request, pk):
    user = request.user
    articles = Article.objects.filter(author=user)
    user_profile = UserProfile.objects.get(user=user)
    fm = UserProfileForm()
    context = {'profile':user_profile, "articles":articles, 'fm':fm} 
    return render(request, 'blog/profile.html', context=context)
    #return HttpResponse(user)


@login_required(login_url='login')
def change_profile_photo(request):
    uprofile = UserProfile.objects.get(id=request.user.id)
    print(request.FILES)
    uprofile.image = request.FILES['image']
    uprofile.bio = request.POST['bio']
    uprofile.save()
    # uprofile.image = request.FILES['image']
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))