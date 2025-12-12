
from django.shortcuts import render
from blogs.models import Blog,Category

def home (request):
    
    # categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured = True ,  status='published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured = False, status='published')
    # # print(featured_posts)
    # print(categories)
    # print(posts)
    context ={
        # 'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,

    }

    return render(request, 'home.html',context)