from django.shortcuts import render,redirect
from .models import Profile
from .forms import ContactForm,ProfileForm
# Create your views here.
def profile_list(request):
    profiles=Profile.objects.all()
    return render(request, 'memo/profile_list.html',{'profiles':profiles})


def profile_id(request, profile_id):
    profile=Profile.objects.get(id=profile_id)
    return render(request, 'memo/profile_id.html',{'profile': profile})

def contactView(request):

   if request.method == 'POST':
       form = ContactForm(request.POST)
        
       if form.is_valid():
            print(f"Name:{form.cleaned_data['name']}")
            print(f"Email:{form.cleaned_data['email']}")
            print(f"Message:{form.cleaned_data['message']}")
   else:
       form = ContactForm()
   
   return render(request, 'memo/contact.html',{'form': form})




# profile form
def NewProfileView(request):

   if request.method == 'POST':
       form = ProfileForm(request.POST, request.FILES)
        
       if form.is_valid():
            form.save()
            return redirect('memo:profilelist')
   else:
       form = ProfileForm()
   
   return render(request, 'memo/new_profile.html',{'form': form})