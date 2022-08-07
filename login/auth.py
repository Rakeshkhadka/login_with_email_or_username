from django.contrib.auth.backends import BaseBackend   #list of all autenticated users
from django.contrib.auth import get_user_model #get user_id
from django.db.models import Q
from django.shortcuts import get_object_or_404


Users = get_user_model()

class Email_or_Username(BaseBackend):
    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
    def authenticate(self, request, username=None, password=None):
        try:
            user = Users.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
            if user.check_password(password):
                return user
        except Users.DoesNotExist:
            return None