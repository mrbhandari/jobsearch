from django import forms
from django.core.validators import MinLengthValidator

from authdemo.models import DemoUser, UserProfile



#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User



class DemoUserEditForm(forms.ModelForm):
    """Form for viewing and editing name fields in a DemoUser object.

    A good reference for Django forms is:
    http://pydanny.com/core-concepts-django-modelforms.html
    """

    def __init__(self, *args, **kwargs):
        # TODO: this doesn't seem to work. Need to get to the bottom of it.
        #self.base_fields["display_name"].min_length = 2
        #self.base_fields["display_name"].validators.append(MinLengthValidator)
        #print self.base_fields['display_name'].validators
        super(forms.ModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = DemoUser
        fields = ('first_name', 'last_name', 'display_name')
        fields += ( 'age', 'currently_employed', 'paid_job_before' )
        
            
    def signup(self, request, user):
        wsData = DemoUser()
        wsData.user = user
        
        wsData.zipcode = self.cleaned_data['zipcode']
        wsData.age = self.cleaned_data['age']
        wsData.currently_employed = self.cleaned_data['currently_employed']
        wsData.paid_job_before = self.cleaned_data['paid_job_before']
        wsData.education_level = self.cleaned_data['education_level']
        
        #wsData.wsUser = self.cleaned_data['wsUser']
        #wsData.wsPwd = self.cleaned_data['wsPwd']
        
        wsData.save()
    


#
class DemoUserAdminForm(forms.ModelForm):

    class Meta:
        model = DemoUser
        fields = ('email', 'first_name', 'last_name', 'display_name', 'is_staff', 'is_active', 'date_joined')

    def is_valid(self):
        #log.info(force_text(self.errors))
        return super(DemoUserAdminForm, self).is_valid()
