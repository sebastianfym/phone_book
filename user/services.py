import random
import smtplib

from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import user_logged_in


def get_access_token(user, request):
    token = str(RefreshToken.for_user(user).access_token)
    user_logged_in.send(sender=user.__class__, request=request, user=user)
    return token