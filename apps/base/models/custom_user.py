import re

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.exceptions import ValidationError
from django.db import models


def validate_phone_number(value):
    if not re.fullmatch(r"^\+?\d{10,15}$", value):
        raise ValidationError(
            "Phone number must be between 10 and 15 digits, optionally starting with '+'."
        )


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("user_type", "office_staff")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Admin must have is_staff=True.")
        if extra_fields.get("user_type") != "office_staff":
            raise ValueError('Admin must have user_type="office_staff".')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICE = (
        ("office_staff", "Office_Staff"),
        ("field_staff", "Field_Staff"),
        ("customer", "Customer"),
    )
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=16, validators=[validate_phone_number])
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(
        max_length=15, choices=USER_TYPE_CHOICE, default="customer"
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "phone"]

    def __str__(self):
        return self.email
