"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^aypaf)x48l)2im7&fa+n&3f0v8_lqdb4padz^@9f0x-7hz*#!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['ultimatefitapp.azurewebsites.net', 'localhost']


# Application definition

INSTALLED_APPS = [    
    'ultimatefitbackend',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    #'django_crontab',
    "django_cron",
    'multiselectfield',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ultimatefit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'ultimatefitbackend.context_processor_file.translation_dictionary',
                'ultimatefitbackend.context_processor_file.render_total_cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'ultimatefit.wsgi.application'

AUTHENTICATION_BACKENDS = (
    # 'social.backends.facebook.FacebookOAuth2',
    # 'social_core.backends.facebook.FacebookOAuth2'
    'django.contrib.auth.backends.ModelBackend',
)

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

CART_PRODUCT_MODEL = 'products.models.Product'

LANGUAGES = (
    ('en', _('English')),
    ('vn', _('Vietnamese')),
)

LANGUAGE_CODE = 'en-us'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'Singapore'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_ROOT = 'D:\home\site\wwwroot\static'
STATIC_URL = '/static/'
SITE_ROOT = os.path.join(os.path.dirname(os.path.realpath(__file__)),"..")
STATICFILES_DIRS = (
  os.path.join(SITE_ROOT, 'ultimatefitbackend/static/'),
)

# Registration
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
LOGIN_REDIRECT_URL = '/cart'

# Email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST", '')
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", '')
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", '')
EMAIL_PORT = os.environ.get("EMAIL_PORT", '')
#EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
#DEFAULT_FROM_EMAIL = "ntu.theanh@yahoo.com"
DEFAULT_FROM_EMAIL = "noreply@ultimate.fit"

# Email settings
'''
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "twohourbinhyen@gmail.com"
EMAIL_HOST_PASSWORD = "iahk9425"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "twohourbinhyen@gmail.com"
'''

# Session expire
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 4 * 7 * 24 * 60 * 60

'''CRONJOBS = [
    ('*/1 * * * *', 'ultimatefitbackend.cron.my_scheduled_job')
    #('*/1 * * * *', 'ultimatefitbackend.cron.my_scheduled_job', '> cron.log')
]
CRONTAB_COMMAND_SUFFIX = "2>&1"'''

CRON_CLASSES = [
    "ultimatefitbackend.cron.MyCronJob",
    # ...
]