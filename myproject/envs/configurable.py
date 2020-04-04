from .base import *

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql",
        'NAME': get_secret_setting("DATABASE_NAME"),
        'USER': get_secret_setting("DATABASE_USER"),
        'PASSWORD': get_secret_setting("DATABASE_PASSWORD"),
        'HOST': get_secret_setting("DATABASE_HOST"),
        'PORT': get_secret_setting("DATABASE_PORT"),
    }
}
