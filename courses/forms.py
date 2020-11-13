from django import forms
from .models import Submission
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#class SubmissionForm(forms.ModelForm):
#    class Meta:
#        model = Submission
#        fields = {'title', 'sub'}



class UserRegisterForm(UserCreationForm):
	

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name in ('username','email', 'password1', 'password2'):
            self.fields[field_name].help_text = ""
        self.fields['email'].required = True
