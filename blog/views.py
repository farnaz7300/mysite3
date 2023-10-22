from django.http.response import Http404
from django.shortcuts import render 
from blog.models import Post , Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def blog_view(request,cat_name=None,author_username=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts=posts.filter(category__name=cat_name)
    if author_username:
        posts=posts.filter(author__username=author_username)
    posts = Paginator(posts,3)
    try:
        page_number=request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
        if kwargs.get('tag_name')!=None:
            posts=posts.filter(tag__name__in=[kwargs['tag_name']])
    context = {'posts': posts}
    return render(request,'blog/blog.html',context)

    
def blog_detail(request):
    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
    posts= Post.objects.filter(status=1)
    comments=Comment.objects.all()
    form=CommentForm()
    context = {'posts': posts , 'comments':comments , 'form':form}
    return render(request,'blog/detail.html',context)

def blog_category(request,cat_name):
    posts=Post.objects.filter(status=1)
    posts=posts.filter(category_name=cat_name)
    context={'post':post}
    return render(request,'blog/blog-home.html',context)

def blog_search (request):
    posts=Post.objects.filter(status=1)
    if request.method =='GET':
        if s:= request.GET.get('s'):
            posts=posts.filter(content__contains=s)
    context={'posts':posts}
    return render(request,'blog/blog.html',context)
# Create your views here.
