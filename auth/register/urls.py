from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from .views import CustomUserViewSet
# from rest_framework_simplejwt.views import TokenRefreshView
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



from . import views
router = DefaultRouter()
# router.register(r'', CustomUserViewSet)
urlpatterns = [
    # path("", views.RegisterView.as_view(), name="register"),
    # path("login/", TokenObtainPairView.as_view(), name="login"),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

        path("", include(router.urls)),
]