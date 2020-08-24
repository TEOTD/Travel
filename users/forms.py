from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,comment
from blog.models import Book


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password1', 'password2']

class CommentForms(forms.ModelForm):
    name = forms.TextInput()
    email = forms.EmailField()
    How_Did_You_Find_Us = forms.Textarea()
    Leave_us_a_line = forms.Textarea()

    class Meta:
        model = comment
        fields = ['name','email','How_Did_You_Find_Us','Leave_us_a_line']

class BookingForm(forms.ModelForm):
    name = forms.TextInput()
    phno = forms.CharField(max_length=12)

    class Meta:
        model = Book
        fields = ['name','phno']




class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
