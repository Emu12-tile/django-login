from django.urls import path,include
from rest_framework.routers import DefaultRouter


from .views import  TodoListCreateView,TodoUpdateView,TodoDeleteView

# router = DefaultRouter()
urlpatterns = [
    path("", TodoListCreateView.as_view(), name="register"),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='todo-delete'), 
    path('update/<int:pk>/', TodoUpdateView.as_view(), name='todo-update'), 

    # path("", include(router.urls)),
]