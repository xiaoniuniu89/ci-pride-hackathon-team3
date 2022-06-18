from django.shortcuts import render
from .models import Profile
# Create your views here.
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'user_profile/profile.html', {'profile': profile})