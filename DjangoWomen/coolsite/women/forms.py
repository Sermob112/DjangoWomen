from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *
class AddPostForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['cat'].empty_label = 'Категория не выьранна'

    class Meta:
        model = Women
        fields = ['title','slug','content','photo','is_published','cat']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-input'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if(len(title)) > 200:
            raise ValidationError('Слишком большая длина')

        return title
    # title = forms.CharField(max_length=255, label='Заголовок', widget=forms.TextInput(attrs={'class':'form-input'}))
    # slug = forms.SlugField(max_length=255)
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}))
    # is_published = forms.BooleanField(required=False, initial=True)
    # cat = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label='Категория не выбрана')


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Email',widget=forms.EmailInput(attrs={'class':'form-input'}))

    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, label='Имя')
    email = forms.EmailField(max_length=255, label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}), label='Контент')
    captcha = CaptchaField()