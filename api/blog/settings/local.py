from .base import *

DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'blog',
       'USER': 'postgres',
       'PASSWORD': 'SANTIjunco11',
       'HOST': 'localhost',
       'PORT': '5432'
   }
}