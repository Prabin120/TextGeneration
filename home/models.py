from django.db import models
from user.models import User

# Create your models here.
class Summary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="summaries")
    prompt  = models.TextField(null=False)
    result = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prompt[:50]}..." if len(self.prompt) > 50 else self.prompt
    

class BulletPoint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bullet_points")
    prompt  = models.TextField(null=False)
    result = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prompt[:50]}..." if len(self.prompt) > 50 else self.prompt