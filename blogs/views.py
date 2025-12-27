from django.http import HttpResponseRedirect
from django.shortcuts import render , get_object_or_404 , redirect
from django.db.models import Q
from .models import Blog ,Category, Comment

def posts_by_category(request, category_id):
    #Fatch the post that belongs to the category with the Id category_id
    # print(category_id)
    posts= Blog.objects.filter(status='Published',category = category_id)
    # Use trey /except when we want to do some custom action if the category doesn't exist 
    try: 
        category = Category.objects.get(pk=category_id)
    except:
        # Redirect the user to homepage 
        return redirect('home')
    
    # Use get_object_or_404 when you want to show 404 error page if the category doesn't exist 
    # category = get_object_or_404(Category, pk=category_id)
  
    context={
        'posts': posts,
        'category':category,
    }
    return render (request , 'posts_by_category.html', context)

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status= 'Published')
    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        print(comment.created_at)
        return HttpResponseRedirect(request.path_info)

    #Comments
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count()
 
    context = {
        'single_blog': single_blog,
        'comments':comments,
        'comment_count':comment_count,
        }
    return render(request, 'blogs.html',  context)

def search(request):
    keyword= request.GET.get('keyword')
    print('keyword==>', keyword)

    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status ="Published")

    context={
        'blogs': blogs , 
        'keyword' : keyword
    }
    return render(request,'search.html', context)

