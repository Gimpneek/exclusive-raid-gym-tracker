# -*- coding: utf-8 -*-
""" Views for Sign up form """
from logging import getLogger
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app.models.profile import Profile
from app.forms.user import UserForm
from rest_framework_jwt.settings import api_settings


LOGGER = getLogger(__name__)


@csrf_exempt
def signup_page(request):
    """
    Show Sign up page for GET request. If unable to create account then show
    errors. If successful then redirect to the Gym List
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            Profile.objects.create(user=new_user)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
            payload = jwt_payload_handler(new_user)
            token = jwt_encode_handler(payload)
            return JsonResponse({'token': token})
        else:
            LOGGER.warning(
                'Issues signed up with %s', form.data.get('username'))
            return JsonResponse(form.errors, status=400)
