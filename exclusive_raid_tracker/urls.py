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
from rest_framework_nested import routers
from rest_framework_jwt.views import obtain_jwt_token
from app.views.homepage import index
from app.views.view_sets.gym_view_set import GymViewSet
from app.views.view_sets.gym_item_view_set import GymItemViewSet
from app.views.view_sets.raid_item_view_set import RaidItemViewSet
from app.views.view_sets.profile_view_set import ProfileViewSet
from app.views.view_sets.personalised_gym_view_set import UserGymViewSet
from app.views.view_sets.personalised_gym_item_view_set import \
    UserGymGymItemViewSet, UserGymItemViewSet
from app.views.view_sets.personalised_raids_view_set import UserRaidsViewSet
from app.views.view_sets.gym_raids_view_set import GymRaidsViewSet
from app.views.view_sets.personalised_profile_view_set import \
    UserProfileViewSet

system_wide_router = routers.DefaultRouter()
system_wide_router.register(r'gyms', GymViewSet, base_name='system_gyms')
system_wide_router.register(r'gym-visits', GymItemViewSet)
system_wide_router.register(r'raids', RaidItemViewSet)
system_wide_router.register(r'profiles', ProfileViewSet, base_name='profiles')
system_wide_router.register(r'me', UserProfileViewSet, base_name='me')

gym_raids_router = routers.NestedSimpleRouter(
    system_wide_router,
    r'gyms',
    lookup='system_gyms'
)

gym_raids_router.register(
    r'raids',
    GymRaidsViewSet,
    base_name='system_raids'
)

personalised_router = routers.DefaultRouter()
personalised_router.register(
    r'gyms',
    UserGymViewSet,
    base_name='personalised_gyms'
)

personalised_router.register(
    r'visits',
    UserGymItemViewSet,
    base_name='personalised_visits'
)

personalised_router.register(
    r'raids',
    UserRaidsViewSet,
    base_name='personalised_raids'
)

personalised_visits_router = routers.NestedSimpleRouter(
    personalised_router,
    r'gyms',
    lookup='personalised_gyms'
)

personalised_visits_router.register(
    r'visits',
    UserGymGymItemViewSet,
    base_name='personalised_gym_visits'
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(system_wide_router.urls)),
    url(r'^api/v1/', include(gym_raids_router.urls)),
    url(r'^api/v1/me/', include(personalised_router.urls)),
    url(r'^api/v1/me/', include(personalised_visits_router.urls)),
    url(r'^api/v1/api-token-auth/', obtain_jwt_token),
    url(r'', index, name='index'),
]
