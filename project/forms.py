from django.forms import ModelForm, TextInput, Textarea
from .models import Post

class Blog_Form(ModelForm):
    class Meta:
        model=Post
        fields=["title","author","description","code","conclusion"]
        widgets={
            "title":TextInput(attrs={"class":"input","placeholder":"Add title"}),
            "author":TextInput(attrs={"class":"input","placeholder":"Author??"}),
            "description":Textarea(attrs={"class":"form-control","placeholder":"Main writing"}),
            "code":Textarea(attrs={"class":"form-control","placeholder":"the code?"}),
            "conclusion":Textarea(attrs={"class":"form-control","placeholder":"khatm karde bhai"})
        }