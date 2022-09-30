from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from poll_api.views import UserViewSet, PollViewSet, ParticipantViewSet, ChoiceViewSet, VoteViewSet

router = routers.SimpleRouter()
router.register('user', UserViewSet, basename='user')
router.register('poll', PollViewSet, basename='poll')
router.register('participant', ParticipantViewSet, basename='participant')
router.register('choice', ChoiceViewSet, basename='choice')
router.register('vote', VoteViewSet, basename='vote')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls))
]