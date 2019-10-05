from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from .models import User, Vendor
from django.db import transaction
from django.utils.translation import gettext_lazy as _

# Create the form class.
#Form to create User as a Vendor during signup 
class VendorForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        #fields = fields = '__all__'
        #We donot need all fields to be filled by the Vendor at Signup time,so avoiding

        fields = ('email','username',)
        # If fields to be used during signup are less in number, this can be used
        # exclude = ['fields'] can also be used to list the fields that be don't want
        # during signup
        help_texts = {
            'username': None,
            'email': None,
        }
        # help text is used to avoid Django creting unnecessary Test during Signup Form
        #exclude = ['title']
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_vendor = True
        # To make the is_vendor flag = True, so as to make a differentiation between
        # diferent type of users.
        user.save()
        return user

class CustomerForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email','username',)
        help_texts = {
            'username': None,
            'email': None,
        }
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        return user


class UpdateProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email', 'phone','gender', 'first_name', 'last_name', 'address','pincode','city','state')
        # labels = {
        #     'gender': _('Gender'),
        # }
        help_texts = {
            'username': _("username is unique, you can't change it"),
        }
        error_messages = {
            'phone': {
                'max_length': _("Phone number must be of 10 digits"),
            },
        }

    
    def __init__(self, *args, **kwargs):
       super(UpdateProfile, self).__init__(*args, **kwargs)
       self.fields['username'].widget.attrs['readonly'] = True