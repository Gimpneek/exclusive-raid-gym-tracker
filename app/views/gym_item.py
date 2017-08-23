""" Views for homepage """
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models.gym_item import GymItem
from app.forms.gym_item import GymItemForm


@login_required
def gym_item(request, gym_item_id):
    """
    Show the homepage
    """
    gym_item = GymItem.objects.get(id=gym_item_id)
    if request.POST:
        form = GymItemForm(request.POST)
        if form.is_valid():
            last_visit_date = request.POST['last_visit_date']
            gym_item.last_visit_date = last_visit_date
            gym_item.save()
            return redirect('gym_list')
    else:
        form = GymItemForm()
    return render(request, 'app/gym_item.html', {
        'gym_item': gym_item,
        'form': form
    })
