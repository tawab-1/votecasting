from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home.api.v1.views import PartyViewSet, CandidateViewSet

router = DefaultRouter()

router.register('party', PartyViewSet, basename='party')
router.register('candidate', CandidateViewSet, basename='candidate')

urlpatterns = [
    path('', include(router.urls))
]