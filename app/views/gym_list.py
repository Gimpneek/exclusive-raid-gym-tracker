""" Views for homepage """
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models.gym_item import GymItem
from app.models.profile import Profile
from django.db.models import F


@login_required
def gym_list(request):
    """
    Show the homepage
    """
    profile = Profile.objects.get(user=request.user.id)
    gym_list = GymItem.objects.filter(profile=profile.id, hidden=False).order_by(F('last_visit_date').asc(nulls_first=True), 'gym__name')
    total_gyms = len(gym_list)
    completed_gyms = len([g for g in gym_list if g.last_visit_date])
    return render(request, 'app/gym_list.html', {
        'gym_list': gym_list,
        'total_gyms': total_gyms,
        'completed_gyms': completed_gyms,
        'gym_progress': int((float(completed_gyms)/float(total_gyms))*100)
    })
