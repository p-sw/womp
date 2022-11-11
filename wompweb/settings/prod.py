from secrets import token_hex
from .base import *

SECRET_KEY = token_hex(32)

DEBUG = False

ALLOWED_HOSTS = ["womp.sserve.work"]
CSRF_TRUSTED_ORIGINS = ["https://womp.sserve.work"]
