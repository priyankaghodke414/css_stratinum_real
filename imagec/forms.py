from django import forms
from .models import Album
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import	Post

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['image']

#from .models import User


class EditProfileForm(UserChangeForm):
    template_name = '/something/else'

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password'

        )


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('Penname','AboutMe')