
from django.shortcuts import render
from blogs.models import Blog,Category
from assignments.models import About
# from .form import RegistrationFrom
def home (request):
    
    # categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured = True ,  status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured = False, status='Published')
    # # print(featured_posts)
    # print(categories)
    # print(posts)

#  fetch about us
    try: 
        about = About.objects.get()
    except:
        about = None 

    context ={
        # 'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
        'about' : about ,

    }
    print(context)
    return render(request, 'home.html',context)


# def register(request):
#     form = RegistrationFrom()
#     context ={
#         'form':form , 
#     }
#     return render(request,'register.html',context)