from .base import *  # noqa: F401, F403

DEBUG = False

_PLACEHOLDER_SECRETS = {"", "change-me-to-a-random-string"}
for _name, _value in (
    ("SECRET_KEY", SECRET_KEY),  # noqa: F405
    ("ENCRYPTION_KEY_SALT", (ENCRYPTION_KEY_SALT or b"").decode("utf-8")),  # noqa: F405
):
    if _value in _PLACEHOLDER_SECRETS or _value.startswith("change-me"):
        if _name == "ENCRYPTION_KEY_SALT" and _value == "" and SECRET_KEY == "build-placeholder":  # noqa: F405
            continue
        from django.core.exceptions import ImproperlyConfigured

        raise ImproperlyConfigured(
            f"{_name} is unset or still the .env.example placeholder. Generate a random value "
            "(e.g. python -c 'import secrets; print(secrets.token_urlsafe(50))') before running in production."
        )

# Security
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_REDIRECT_EXEMPT = [r"^health/$"]

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "WARNING",
            "propagate": False,
        },
        "apps": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "gunicorn.error": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
