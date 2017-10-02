"""exclusive_raid_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from app.views.homepage import index
from app.views.login import login_page
from app.views.logout import logout_page
from app.views.gym_list import gym_list
from app.views.signup import signup_page
from app.views.change_gym_item import remove_gym_item, hide_gym_item, \
    add_gym_raid
from app.views.user_profile import user_profile
from app.views.analytics_dashboard import analytics_dashboard
from app.views.view_sets.gym_view_set import GymViewSet
from app.views.view_sets.gym_item_view_set import GymItemViewSet

api_router = routers.DefaultRouter()
api_router.register(r'gyms', GymViewSet)
api_router.register(r'gym-visits', GymItemViewSet)


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login_page, name='login'),
    url(r'^logout/$', logout_page, name='logout'),
    url(r'^signup/$', signup_page, name='signup'),
    url(r'^list/$', gym_list, name='gym_list'),
    url(r'^profile/$', user_profile, name='profile'),
    url(r'^analytics/$', analytics_dashboard, name='analytics'),
    url(r'^add/(?P<gym_id>\d+)/$', add_gym_raid, name='add_gym_raid'),
    url(r'^hide/(?P<gym_item_id>\d+)/$', hide_gym_item, name='hide_gym_item'),
    url(r'^remove/(?P<gym_item_id>\d+)/$',
        remove_gym_item,
        name='remove_gym_item'
        ),
    url(r'^api/v1/', include(api_router.urls))
]
