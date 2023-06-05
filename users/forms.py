from django import forms
from django.core.exceptions import ValidationError
from .models import User, Profile, ProfileImage
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required fields,
    plus a repeated password
    """
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ['email']

    def clean_password2(self):
        # Check that two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError(_('Passwords dont match'))
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admins
    disabled password hash display field
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['email', 'password', 'is_active', 'is_admin']


class ProfileCreationForm(forms.ModelForm):
    """
    A form for creating profiles of users
    """
    class Meta:
        model = Profile
        fields = ('name', 'date_of_birth', 'gender', 'looking_for',
                  'sexual_identity', 'bio', 'interest', )


class ProfileImageForm(forms.ModelForm):
    """
    A form for profile images
    """
    class Meta:
        model = ProfileImage
        fields = ('image', )
