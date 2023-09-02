from django.shortcuts import render
from .models import Profile
# Create your views here.
def profile_list(request):
    profiles=Profile.objects.all()
    return render(request, 'memo/profile_list.html',{'profiles':profiles})


def profile_id(request, profile_id):
    profile=Profile.objects.get(id=profile_id)
    return render(request, 'memo/profile_id.html',{'profile': profile})