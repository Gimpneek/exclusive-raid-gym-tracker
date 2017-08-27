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
from django.conf.urls import url
from app.views.homepage import index
from app.views.login import login_page
from app.views.logout import logout_page
from app.views.gym_list import gym_list
from app.views.signup import signup_page
from app.views.gym_item import gym_item
from app.views.hide_gym_item import hide_gym_item
from app.views.reset_gym_item import reset_gym_item
from django.contrib import admin

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login_page, name='login'),
    url(r'^logout/$', logout_page, name='logout'),
    url(r'^signup/$', signup_page, name='signup'),
    url(r'^list/$', gym_list, name='gym_list'),
    url(r'^item/(?P<gym_item_id>\d+)/$', gym_item, name='gym_item'),
    url(r'^hide/(?P<gym_item_id>\d+)/$', hide_gym_item, name='hide_gym_item'),
    url(r'^reset/(?P<gym_item_id>\d+)/$', reset_gym_item, name='reset_gym_item'),
]
