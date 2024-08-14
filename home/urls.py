from django.urls import path
from .views import GenerateBulletPoints, GenerateSummary

urlpatterns = [
    path('generate-summary/', GenerateSummary.as_view(), name="generate-summary"),
    path('generate-bullet-points/', GenerateBulletPoints.as_view(), name="generate-bullet-points"),
]
