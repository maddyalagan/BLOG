from django.shortcuts import render,redirect
from .models import Blog
from django.core.paginator import Paginator
import os

# Create your views here.


def home(request):
    blog_obj = Blog.objects.all()
    blog_name = request.GET.get("blog_name")
    if blog_name != "" and blog_name is not None:
        blog_obj = blog_obj.filter(title__icontains=blog_name)
    paginator = Paginator(blog_obj,4)
    page = request.GET.get('page')
    blog_obj = paginator.get_page(page)
    return render(request,"home.html",{"blogs":blog_obj})

def add_new_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")
        if title and image:
            Blog.objects.create(title=title,content= content,image=image)
            
            return redirect("home_page")
    return render(request,"add_blog.html")

def update_old_blog(request,id):
    blog_obj = Blog.objects.get(id=id)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")
        blog_obj.title = title
        blog_obj.content = content
        if image:
            if blog_obj.image:
                if os.path.exists(blog_obj.image.path):
                    os.remove(blog_obj.image.path)
                blog_obj.image= image
            blog_obj.save()
            return redirect("home_page")
    return render(request,"update_blog.html",{"blog":blog_obj})

def delete_old_blog(request,id):
    blog_obj = Blog.objects.get(id=id)
    blog_obj.delete()
    return redirect("/")