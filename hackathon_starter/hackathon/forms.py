from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from hackathon.models import UserProfile





#class UserForm(forms.ModelForm):
#    password = forms.CharField(widget=forms.PasswordInput())
#
#    class Meta:
#        model = User
#        fields = ('username', 'email', 'password')


class SignupForm(forms.ModelForm):
    #wsUser = forms.CharField(max_length=40, label='WS Username')
    #wsPwd  = forms.CharField(max_length=40, label='WS Password')
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        
        
    def signup(self, request, user):
        wsData = UserProfile()
        wsData.user = user
        
        wsData.zipcode = self.cleaned_data['zipcode']
        wsData.age = self.cleaned_data['age']
        wsData.currently_employed = self.cleaned_data['currently_employed']
        wsData.paid_job_before = self.cleaned_data['paid_job_before']
        wsData.education_level = self.cleaned_data['education_level']
        
        #wsData.wsUser = self.cleaned_data['wsUser']
        #wsData.wsPwd = self.cleaned_data['wsPwd']
        
        wsData.save()
    class Meta:
        model = UserProfile
        fields = ('zipcode', 'age', 'currently_employed', 'paid_job_before', 'education_level' )
        #fields = ('wsUser', 'wsPwd',)
        
        

