from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


class EmailLoginBackend(object):
    """
    Authenticate against the email of user'
    """

    def authenticate(self, request, email=None, password=None):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

