from django.urls import path,include
from .views import UserListSet 
from rest_framework.routers import DefaultRouter
from .views import RegisterView,LoginView
# from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



from . import views
router = DefaultRouter()
router.register(r"", UserListSet, basename="register")
urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

        path("", include(router.urls)),
]