from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.
class UserView(APIView):
    """
    API endpoint for user registration and retrieval.
    
    * **post**: Register a new user.
    * **get**: Retrieve the authenticated user's information.
    """
    def get_permissions(self):
        """
        Set different permissions for GET and POST requests.
        """
        if self.request.method == 'POST':
            return [AllowAny()]
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return super().get_permissions()

    def get(self,request):
        """
        Retrieve the authenticated user's information.

        **Permissions**: Authenticated users only.
        """
        username = request.user
        try:
            user = User.objects.get(username = username)
        except:
            return Response({"message":"invalid user"}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        """
        Register a new user.

        **Permissions**: Open to all users.

        **Required fields**: `username`, `password`, `confirm_password`

        **Optional fields**: `name`
        """
        username = request.data.get('username')
        name = request.data.get('name','')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        if not(username and password and confirm_password):
            return Response({"message": "username, password and confirm password are required"}, status=status.HTTP_400_BAD_REQUEST)
        if password != confirm_password:
            return Response({"message": "password and confirm password are not equal"}, status=status.HTTP_400_BAD_REQUEST)

        if(User.objects.filter(username = username).exists()):
            return Response({"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User(username = username, name = name)
        user.set_password(password)
        user.save()
        serializer = UserSerializer(user)
        refresh = RefreshToken.for_user(user)
        return Response({"user":serializer.data,
                         "access":str(refresh.access_token),
                         "refresh":str(refresh)}, 
                        status=status.HTTP_200_OK)
    

class Login(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if(not(username and password)):
            return Response({"message":"Username and password required"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.filter(username=username).first()
        if not user:
            return Response({"message": "Username doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)
        if not authenticate(username=username, password=password):
            return Response({"message":"Username or password wrong"}, status=status.HTTP_403_FORBIDDEN)
        serializer = UserSerializer(user)
        refresh = RefreshToken.for_user(user)
        return Response({"user":serializer.data,
                         "access":str(refresh.access_token),
                         "refresh":str(refresh)}, 
                        status=status.HTTP_200_OK)