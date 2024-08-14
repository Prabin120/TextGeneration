from django.urls import path
from .views import UserView, Login
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('',UserView.as_view()),
    path('sign-in/',Login.as_view()),
    # path('sign-out/',UserView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
]