from django import forms
from .models import Post


class PostForm(forms.Form):
    title=forms.CharField()
    description=forms.CharField()



class PostModelForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','description','image','slug']




class UserModelForm(forms.ModelForm):
    class Meta:
        pass