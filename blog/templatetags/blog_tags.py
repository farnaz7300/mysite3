from django import template
from blog.models import Post
from blog.models import Category

register = template.Library()

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.simple_tag(name='comment_count')
def function(pid):
    Post = Post.objects.get(pk=pid)
    return Comment.objects.filter(post=post.id,approved=True).count()


@register.filter
def snippet(value,arg=20):
    return value[:arg]+'...'

@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts():
    posts=Post.objects.filter(status=1).order_by('published_date')[:1]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts=Post.objects.filter(status=1)
    categories=Category.objects.all()
    cat_dict={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}