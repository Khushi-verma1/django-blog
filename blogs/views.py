from django.shortcuts import render , get_object_or_404 , redirect

from .models import Blog,Category

def posts_by_category(request, category_id):
    #Fatch the post that belongs to the category with the Id category_id
    # print(category_id)
    posts= Blog.objects.filter(status='published',category = category_id)
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
