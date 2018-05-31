from django.shortcuts import render
from .models import Profile



def profile(request):
    # user = Profile.objects.all().first()
    return render(request, 'accounts/profile.html')