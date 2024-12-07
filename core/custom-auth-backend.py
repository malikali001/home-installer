from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class CustomBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.filter(email=email).first()
            if user is None:
                user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
