from django.urls import path
from .views import UserView, Login
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('',UserView.as_view(), name='user'),
    path('sign-in/',Login.as_view(), name="sign-in"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
]