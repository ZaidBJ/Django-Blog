from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Author
# Create your views here.
from .forms import PostModelForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  login,logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




@login_required()
def posts_list(request):
    authora, created = Author.objects.get_or_create(user=request.user)
    all_posts=Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(all_posts, 2)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    print(request.user)
    context={"users":users,"author":authora}
    return render(request,"posts/posts_list.html",context)


@login_required()
def posts_detail(request,slug):
    unique_post=get_object_or_404(Post,slug=slug)
    authora, created = Author.objects.get_or_create(user=request.user)
    context={'post':unique_post,"author":authora}

    return render(request,"posts/post_detail.html",context)


def post_create(request):
    print(request.user)

    authora=get_object_or_404(Author,user=request.user)
    if(request.method=="POST"):
     form =PostModelForm(request.POST,request.FILES)
     if form.is_valid():
         form.instance.author=authora
         form.save()
         return redirect('/posts/')


     context={'form':form}
     return render(request,"posts/posts_create.html",context)
    elif (request.method=="GET"):
     form=PostModelForm()
     context = {'form': form}
     return render(request, "posts/posts_create.html", context)

@login_required()
def posts_update(request,slug):
  uniq_post=get_object_or_404(Post,slug=slug)
  print(request.user.username)
  print(uniq_post.author)
  if(uniq_post.author.user==request.user):
    if(request.method=="POST"):
        form = PostModelForm(request.POST,request.FILES,instance=uniq_post)  # instance to pre populate the form
        context={'form':form}
        if (form.is_valid()):
            form.save()
            return redirect("/posts")
    else:
        form= PostModelForm(instance=uniq_post)
        context = {'form': form}

    return render(request,"posts/posts_update.html",context)
  else:
    return render(request, "posts/posts_fail.html")


@login_required()
def posts_delete(request,slug):
    uniq_post=get_object_or_404(Post,slug=slug)
    uniq_post.delete()
    return redirect("/posts")



def user_create(request):

  if(request.method=="POST"):
    pwd=request.POST.get('pp')
    name=request.POST.get('username')
    img=request.FILES['image']

    user =User.objects.create_user(username=name, email="zaidjunaid5@gmail.com",password=pwd)
    author,created = Author.objects.get_or_create(user=user, image=img)
    author.save()
    user.save()
    login(request,user)
    request.user=user
    all_posts = Post.objects.all()
    context={"author":author,"posts":all_posts}
    return render(request,"posts/posts_list.html",context)

  else :
    logout(request)
    return render(request,"posts/form.html")








