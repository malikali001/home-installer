from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create a superuser if it does not already exist"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        email = "admin@example.com"
        password = "adminpassword"
        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(email=email, password=password)
            self.stdout.write(self.style.SUCCESS("Superuser created!"))
        else:
            self.stdout.write(self.style.WARNING("Superuser already exists."))
