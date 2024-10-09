from django.urls import path,include
from .views import UserListSet 
from rest_framework.routers import DefaultRouter

from . import views
router = DefaultRouter()
router.register(r"", UserListSet, basename="register")
urlpatterns = [
    # path("", views.registerPage, name="index"),
        path("", include(router.urls)),
]