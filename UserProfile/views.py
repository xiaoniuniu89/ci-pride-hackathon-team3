from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import UserProfile


@login_required
def Profile(request):

    user_profile = get_object_or_404(UserProfile, user=request.user)
    template = 'UserProfile/profile.html'

    context = {
        'user': request.user
    }

    return render(request, template, context)
