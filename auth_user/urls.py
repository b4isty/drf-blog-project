from django.urls import path

from .views import RegisterView
from .authentication import ObtainAuthToken
app_name = "auth_user"

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('api-token-auth/', ObtainAuthToken.as_view()),

]