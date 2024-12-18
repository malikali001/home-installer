import os
import random
import string
import sys
from pathlib import Path

import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    SECRET_KEY = "".join(random.choice(string.ascii_lowercase) for i in range(32))

# Debug Flag
DEBUG = env.bool("DEBUG", False)

# Assets Management
ASSETS_ROOT = os.getenv("ASSETS_ROOT", "/static/assets")

# load production server from .env
ALLOWED_HOSTS = [
    "localhost",
    "localhost:85",
    "127.0.0.1",
    env("SERVER", default="127.0.0.1"),
]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:85",
    "http://127.0.0.1",
    "https://" + env("SERVER", default="127.0.0.1"),
]


RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
    CSRF_TRUSTED_ORIGINS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "apps.home",  # Enable the inner home (home)
    "apps.authentication",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "allauth.socialaccount.providers.twitter",
    "sslserver",
    "apps.accounts",
    "apps.base",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"
LOGIN_REDIRECT_URL = "home"  # Route defined in home/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in home/urls.py
TEMPLATE_DIR = os.path.join(CORE_DIR, "apps/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "apps.context_processors.cfg_assets_root",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if os.environ.get("DB_ENGINE") and os.environ.get("DB_ENGINE") == "mysql":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DATABASE_NAME"),
            "USER": os.getenv("DATABASE_USER"),
            "PASSWORD": os.getenv("DATABASE_PASSWORD"),
            "HOST": os.getenv("DATABASE_HOST"),
            "PORT": os.getenv("DATABASE_PORT"),
        }
    }
# else:
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": "db.sqlite3",
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(CORE_DIR, "staticfiles")
STATIC_URL = "/static/"

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (os.path.join(CORE_DIR, "apps/static"),)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "base.CustomUser"
#############################################################

if os.getenv("FTP_UPLOAD", default=False):
    try:
        DEFAULT_FILE_STORAGE = os.getenv("upload_cloud_type")
        ftp_username = os.getenv("ftp_username")
        ftp_password = os.getenv("ftp_password")
        ftp_server_url = os.getenv("ftp_server_url")
        ftp_port = os.getenv("ftp_port")
        FTP_STORAGE_LOCATION = (
            f"ftp://{ftp_username}:{ftp_password}@{ftp_server_url}:{ftp_port}"
        )

        # Enable the feature
        FTP_UPLOAD = True
    except Exception as _:

        FTP_UPLOAD = False
        print("FTP credentials not set in the environment")

GITHUB_CLIENT_ID = os.getenv("GITHUB_ID", None)
GITHUB_SECRET = os.getenv("GITHUB_SECRET", None)
GITHUB_AUTH = GITHUB_SECRET is not None and GITHUB_CLIENT_ID is not None

TWITTER_CLIENT_ID = os.getenv("TWITTER_ID", None)
TWITTER_SECRET = os.getenv("TWITTER_SECRET", None)
TWITTER_AUTH = TWITTER_SECRET is not None and TWITTER_CLIENT_ID is not None

AUTHENTICATION_BACKENDS = (
    "core.custom-auth-backend.CustomBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 11

SERVER = env("SERVER", default="127.0.0.1")

if DEBUG:
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http" if sys.argv[1] == "runserver" else "https"
else:
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"  # assumed production http protocol is https

SOCIALACCOUNT_PROVIDERS = {}
if GITHUB_AUTH:
    SOCIALACCOUNT_PROVIDERS["github"] = {
        "APP": {"client_id": GITHUB_CLIENT_ID, "secret": GITHUB_SECRET, "key": ""}
    }
if TWITTER_AUTH:
    SOCIALACCOUNT_PROVIDERS["twitter"] = {
        "APP": {"client_id": TWITTER_CLIENT_ID, "secret": TWITTER_SECRET, "key": ""}
    }

# AWS S3 settings
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_DEFAULT_ACL = os.getenv("AWS_DEFAULT_ACL")
AWS_S3_ENDPOINT_URL = os.getenv("AWS_S3_ENDPOINT_URL")
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
# static settings
AWS_LOCATION = "static"
STATIC_URL = f"https://{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}/"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = (BASE_DIR / "apps/static",)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles"
DEFAULT_FILE_STORAGE = "core.storage_backends.PublicMediaStorage"
