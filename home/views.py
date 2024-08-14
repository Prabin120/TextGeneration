from utils.groq_llm import groqChat
from utils.prompts import promptForGenerateBullePoints, promptForGenerateSummary
from .models import Summary, BulletPoint
from .serializers import SummarySerializer, BulletPointsSerializer
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from user.models import User

# Create your views here.

class GenerateSummary(APIView):
    """
    API endpoint to get summary from the given text.
    
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        **Get the summary from a given text**

        **Permissions**: Only authenticated user.

        **Required fields**: `text`
        """
        user_input = request.data.get('text')
        if not user_input:
            return JsonResponse({"message":"Input text required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(username = request.user)
        except:
            return JsonResponse(status=status.HTTP_401_UNAUTHORIZED)
        prompt  = promptForGenerateSummary(user_input)
        result = groqChat(prompt )
        data = Summary.objects.create(user = user, prompt = user_input, result = result)
        serializer = SummarySerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GenerateBulletPoints(APIView):
    """
    API endpoint to get bullet points from the given text.
    
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        **Get the bullet points from a given text**

        **Permissions**: Only authenticated user.

        **Required fields**: `text`
        """
        user_input = request.data.get('text')
        if not user_input:
            return JsonResponse({"message":"Input text required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(username = request.user)
        except:
            return JsonResponse(status=status.HTTP_401_UNAUTHORIZED)
        prompt = promptForGenerateBullePoints(user_input)
        result = groqChat(prompt)
        data = BulletPoint.objects.create(user = user, prompt = user_input, result = result)
        serializer = BulletPointsSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)