from django import template
from blog.models import Category
from blog.models import  Post
register=template.Library()


@register.inclusion_tag('blog/blog-caregories.html')
def postcategotys():
   posts = Post.objects.filter(status=1)
   categories = Category.objects.all()
   cat_dict = {}
   for category in categories:
      if posts.filter(category=category).exists():  
         cat_dict[category.name] = posts.filter(category=category).count()
   return {'categories': cat_dict}


@register.inclusion_tag('blog/blog-recent-post.html')
def lastposts(arg=5):
    posts=Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts':posts}
