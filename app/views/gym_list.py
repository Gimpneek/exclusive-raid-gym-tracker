""" Views for homepage """
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models.gym_item import GymItem
from app.models.profile import Profile


@login_required
def gym_list(request):
    """
    Show the homepage
    """
    profile = Profile.objects.get(user=request.user.id)
    gym_list = GymItem.objects.filter(profile=profile.id, hidden=False).order_by('last_visit_date')
    return render(request, 'app/gym_list.html', {
        'gym_list': gym_list
    })
