
from django.db import models
from django.contrib.auth.models import User
import random
import string
from django.utils import timezone
from datetime import timedelta

class ConfirmationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_code(self):
        self.code = ''.join(random.choices(string.digits, k=6))
        self.save()

    def __str__(self):
        return f"Код подтверждения для {self.user.username}: {self.code}"


    def is_code_expired(self):

        expiration_time = timedelta(minutes=10)
        return timezone.now() - self.created_at > expiration_time
