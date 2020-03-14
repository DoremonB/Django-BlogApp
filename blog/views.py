from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Post,Profile,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.core.files.storage import FileSystemStorage




def home(request):
    if request.method=='POST':
        login_data = request.POST.dict()
        username = login_data.get("uname")
        password = login_data.get("password")
      
    return render(request,'blog/home.html')

@login_required
def createPost(request):
    if request.method=='POST':
        data=request.POST.dict()
        title=data.get('title')
        content=data.get('content')
        Post.objects.create(title=title,content=content,author=request.user)
        messages.success(request,f'New Post created!')
        return redirect('/blog/mypost/')

    return render(request,'blog/createPost.html')

@login_required
def mypost(request):
    context={
        "posts":Post.objects.filter(author=request.user).order_by('-date_posted')
    }
    return render(request,'blog/mypost.html',context)

@login_required
def updateFormPage(request,pk):
    if request.method=='POST':
        data=request.POST.dict()
        title=data.get('title')
        content=data.get('content')
        Post.objects.filter(pk=pk).update(title=title,content=content)
        messages.success(request,f'Update Successful!')
        return redirect('/blog/mypost/')

    else:
        p=Post.objects.filter(pk=pk)[0]
        context={
            "p":p
        }
        return render(request,'blog/updateFormPage.html',context)

@login_required
def deleteFormPage(request,pk):
    Post.objects.filter(pk=pk).delete()
    messages.success(request,f'Post Successfully Deleted!')
    return redirect('/blog/mypost/')

def allposts(request):
    context={
        "posts":Post.objects.all().order_by('-date_posted')
    }
    return render(request,'blog/allposts.html',context)

def register(request):
    if request.method=='POST':
        data=request.POST.dict()
        username=data.get('username')
        password=data.get('password')
        
        try:
            User.objects.create_user(username=username,password=password)
            u=User.objects.filter(username=username)[0]
            p=Profile(user=u,bio="Default Bio")
            p.save()
            u.profile=p
            u.save()
            messages.success(request,f'Your Acc has been created!')
            return redirect('/blog/mypost/')
        except Exception as e:
            print(e)
            messages.error(request,f'Error!')
            return redirect('/blog/register/')

    else:
        return render(request,'blog/register.html')


@login_required
def profile(request):
    if request.method=='POST':
        if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            data=request.POST.dict()
            bio=data.get('bio')


            p1=Profile.objects.filter(pk=request.user.profile.id)[0]
            p1.image=myfile
            p1.bio=bio
            p1.save()
        messages.success(request,f'Your Profile has been updated!')
        return redirect('/blog/mypost/')

    else:
        context={
            "user":request.user
        }
        return render(request,'blog/profile.html',context)

@login_required
def deleteAccount(request):
    request.user.delete()
    messages.success(request,f'Your Acc has been deleted along with all your posts!')
    return redirect('/blog/allposts/')

@login_required
def commentAdd(request,pk):
    if request.method=='POST':
        data=request.POST.dict()
        cmt=data.get('cmt')
        curr_post=Post.objects.filter(pk=pk).first()
        c=Comment(post=curr_post,author=request.user.username,text=cmt)
        c.save()
        context={
            "post":Post.objects.filter(pk=pk).first()
        }
        return render(request,'blog/commentAdd.html',context)
    else:
        context={
            "post":Post.objects.filter(pk=pk).first()
        }
        return render(request,'blog/commentAdd.html',context)


