from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User, Owner, Room, Tenant
# admin.site.register()


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('phone', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]



class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('phone','is_admin','is_owner','is_tenant')#''
    list_filter = ('is_admin','is_owner','is_tenant')#'is_owner','is_tenant'
    fieldsets = (
        ('Login Details', {'fields': ('phone', 'password')}),
        ('Personal Details',{'fields': ('name','email')}),
        ('Permissions', {'fields': ('is_admin','is_owner','is_tenant')}),#is_owner','is_tenant
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone','password1', 'password2')}
        ),
    )
    search_fields = ('phone','name')
    ordering = ('phone',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.register(Owner)
admin.site.register(Room)
admin.site.register(Tenant)