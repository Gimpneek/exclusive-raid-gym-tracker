from app.models.gym_item import GymItem
from django.forms.models import ModelForm


class GymItemForm(ModelForm):
    class Meta:
        model = GymItem
        fields = ('last_visit_date',)

