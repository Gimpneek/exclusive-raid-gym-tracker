""" Views for homepage """
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models.gym_item import GymItem


@login_required
def gym_list(request):
    """
    Show the homepage
    """
    gym_list = GymItem.objects.order_by('id')
    return render(request, 'app/gym_list.html', {
        'gym_list': gym_list
    })
