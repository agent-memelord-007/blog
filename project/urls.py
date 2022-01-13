from django.urls import path
from .views import SeePost, home, PostView, AddPost, EditPost, YeetPost


urlpatterns=[
    path("",home,name="home"),
    path("posts",PostView.as_view(),name="projects"),
    path("add",AddPost.as_view(),name="Add_Project"),
    path("view/<int:pk>",SeePost.as_view(),name="View_Post"),
    path("edit/<int:pk>",EditPost.as_view(),name="Edit_Post"),
    path("delete/<int:pk>",YeetPost.as_view(),name="Delete_Post"),
]