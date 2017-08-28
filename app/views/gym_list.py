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
    profile = Profile.objects.get(
        user=request.user.id
    )
    gym_list = GymItem.objects.filter(
        profile=profile.id,
        hidden=False
    ).order_by(
        F('last_visit_date').asc(nulls_first=True),
        'gym__name'
    )
    total_gyms = len(gym_list)
    completed_gyms = [gym for gym in gym_list if gym.last_visit_date]
    gyms_to_visit = [gym for gym in gym_list if not gym.last_visit_date]
    gym_progress = 0
    if len(completed_gyms) > 0:
        gym_progress = int((float(len(completed_gyms))/float(total_gyms))*100)
    return render(request, 'app/gym_list.html', {
        'completed_gym_list': completed_gyms,
        'gyms_to_visit': gyms_to_visit,
        'total_gyms': total_gyms,
        'completed_gym_count': len(completed_gyms),
        'gym_progress': gym_progress
    })
