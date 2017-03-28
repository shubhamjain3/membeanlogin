from django import forms

from .models import join,uploads
class NameForm(forms.Form):
    f_name=forms.CharField(label='your first name',max_length=50)
    l_name=forms.CharField(label='your last name',max_length=50)


class EmailForm(forms.Form):
    email=forms.EmailField()
    
class JoinForm(forms.ModelForm):
    class Meta:
        model=join
        fields=['f_name','l_name','email']

class LoginForm(forms.Form):
    class Meta:
        model=join
        fields=['f_name','l_name','email']
        


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
