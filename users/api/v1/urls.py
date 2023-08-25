from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.api.v1.views import LoginViewSet, UserRegistrationView

router = DefaultRouter()
router.register('signup', UserRegistrationView, basename='signup')
router.register('signin', LoginViewSet, basename='login')

urlpatterns = [
    path('', include(router.urls))
]