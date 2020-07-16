from django import forms
from django.contrib.auth.models import User
from blog_app.models import Post,Comment

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['password'].widget.attrs['placeholder'] = 'password'
        self.fields['email'].widget.attrs['placeholder'] = 'email'
        self.fields['username'].widget.attrs.update({'class' : 'usernamereg'})
    class Meta():
        model=User
        fields=('username','email','password')


class PostForm(forms.ModelForm):
    class Meta():
        model=Post
        fields=('author','title','text')

        widgets={
           'title':forms.TextInput(attrs={'class':'textinputclass'}),
           'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model=Comment
        fields=('author','text')

        widgets={
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
