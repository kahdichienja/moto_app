from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'input-text', 'id': 'id_email', 'required': 'true'}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input-text', 'id': 'id_username', 'required': 'true'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'id_password1', 'required': 'true'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'id_password2', 'required': 'true'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input-text', 'id': 'id_username', 'required': 'true'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'id_password', 'required': 'true'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count() == 1:
        #     user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError(
                    "This user Does Not exists in the system")
            if not user.check_password(password):
                raise forms.ValidationError("Password Incorrect")
            if not user.is_active:
                raise forms.ValidationError(
                    "User Is No longer Active. Contact Admin 254797324006")
        return super(UserLoginForm, self).clean(*args, **kwargs)
