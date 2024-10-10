from django.urls import path,include
from .views import UserListSet 
from rest_framework.routers import DefaultRouter
from .views import RegisterView,LoginView

from . import views
router = DefaultRouter()
router.register(r"", UserListSet, basename="register")
urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
        path("", include(router.urls)),
]