from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Post
from .forms import Blog_Form
from django.urls import reverse_lazy
# Create your views here.
def home(request):
    return render(request, "index.html")

class PostView(ListView):
    model=Post
    template_name="posts.html"


class AddPost(CreateView):
    model=Post
    form_class=Blog_Form
    template_name="add_p.html"

class SeePost(DetailView):
    model=Post
    template_name="look.html"


class EditPost(UpdateView):
    model=Post
    form_class=Blog_Form
    template_name="edit_p.html"

class YeetPost(DeleteView):
    model=Post
    template_name="delete.html"
    success_url=reverse_lazy("projects")