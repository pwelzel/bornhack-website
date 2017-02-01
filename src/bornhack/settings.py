import os
from .environment_settings import *

def local_dir(entry):
    return os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        entry
    )

DJANGO_BASE_PATH = os.path.dirname(os.path.dirname(__file__))

WSGI_APPLICATION = 'bornhack.wsgi.application'
ROOT_URLCONF = 'bornhack.urls'


SITE_ID = 1

ADMINS = (
    ('bornhack sysadm', 'sysadm@bornhack.org'),
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'profiles',
    'camps',
    'shop',
    'news',
    'utils',
    'villages',
    'program',
    'info',
    'sponsors',
    'ircbot',

    'allauth',
    'allauth.account',
    'bootstrap3',
]

STATIC_URL = '/static/'
STATIC_ROOT = local_dir('static')
STATICFILES_DIRS = [local_dir('static_src')]
LANGUAGE_CODE = 'en-us'
#USE_I18N = True
#USE_L10N = True
USE_TZ = True
SHORT_DATE_FORMAT = 'd/m-Y'
DATE_FORMAT = 'd/m-Y'
DATETIME_FORMAT = 'd/m-Y H:i'
TIME_FORMAT = 'H:i'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [local_dir('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shop.context_processors.current_order',
                'shop.context_processors.user_has_tickets',
                'camps.context_processors.camp',
            ],
        },
    },
]

LOGIN_REDIRECT_URL = 'profiles:detail'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # Handles login to admin with username
    'allauth.account.auth_backends.AuthenticationBackend', # Handles regular logins
)

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[bornhack] '
ACCOUNT_USERNAME_REQUIRED = False
LOGIN_REDIRECT_URL='/shop/'
LOGIN_URL = '/login/'

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'

BOOTSTRAP3 = {
    'jquery_url': '/static/js/jquery.min.js',
    'javascript_url': '/static/js/bootstrap.min.js'
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    INSTALLED_APPS += ['debug_toolbar', ]
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'console': {
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
