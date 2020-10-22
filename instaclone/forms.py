from django import forms
from .models import Post, Comment,Profile

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ['profile','likes', 'comment','user']
  
class CommentForm(forms.ModelForm):
  class Meta:
   model = Comment
   exclude = ['post','user']
   
