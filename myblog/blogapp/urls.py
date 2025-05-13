from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="home_page"),
    path("add/",views.add_new_blog,name="add_blog"),
    path("update/<int:id>",views.update_old_blog,name="update_blog"),
    path("delete/<int:id>",views.delete_old_blog,name="delete_blog"),
]