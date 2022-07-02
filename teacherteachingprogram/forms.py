from django import forms


class CheckForm(forms.Form):
    code = forms.CharField(label='password', widget=forms.PasswordInput)