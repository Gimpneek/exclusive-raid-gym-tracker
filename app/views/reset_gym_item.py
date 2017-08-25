""" Views for homepage """
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from app.models.gym_item import GymItem


@login_required
def reset_gym_item(request, gym_item_id):
    """
    Show the homepage
    """
    gym_item = GymItem.objects.get(id=gym_item_id)
    gym_item.last_visit_date = None
    gym_item.save()
    return redirect('gym_list')
