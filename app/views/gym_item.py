# -*- coding: utf-8 -*-
""" Views for individual Gym Item """
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models.gym_item import GymItem
from app.forms.gym_item import GymItemForm


@login_required
def gym_item(request, gym_item_id):
    """
    Show the Gym Item that matches the past ID
    """
    requested_gym_item = GymItem.objects.get(id=gym_item_id)
    if request.POST:
        form = GymItemForm(request.POST)
        if form.is_valid():
            last_visit_date = request.POST['last_visit_date']
            requested_gym_item.last_visit_date = last_visit_date
            requested_gym_item.save()
            return redirect('gym_list')
    else:
        form = GymItemForm()
    date_to_show = datetime.now()
    if requested_gym_item.last_visit_date:
        date_to_show = requested_gym_item.last_visit_date
    return render(request, 'app/gym_item.html', {
        'gym_item': requested_gym_item,
        'form': form,
        'date_to_show': date_to_show
    })
