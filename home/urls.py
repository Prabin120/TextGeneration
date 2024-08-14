from django.urls import path
from .views import GenerateBulletPoints, GenerateSummary

urlpatterns = [
    path('generate-summary/', GenerateSummary.as_view()),
    path('generate-bullet-points/', GenerateBulletPoints.as_view()),
]
