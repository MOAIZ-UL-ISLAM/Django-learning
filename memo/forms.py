from django import forms
from . models import Profile
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"