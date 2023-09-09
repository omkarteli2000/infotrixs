from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_set')
    
    def __str__(self) -> str:
        return self.user.username
    
class Messages(models.Model):
    sender = models.ForeignKey(Users, on_delete=models.CASCADE, null=False, blank=False)
    message = models.CharField(max_length=255, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.message