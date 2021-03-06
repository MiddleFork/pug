"""
Django settings for crawlnmine project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5s3an_jk9pd5hc229r1icz1l(_3zt6rhaqr=#(+@b5@&79wzqc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'celery',

    'pug.crawler',
    'pug.miner',
    'pug.agile',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'crawlnmine.urls'

WSGI_APPLICATION = 'crawlnmine.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


# List of modules to import when celery starts.  But crawlnmine.crawlnmine.__init__ will do this
#CELERY_IMPORTS = ("testcele.tasks",)

# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
# CELERY_RESULT_BACKEND = "database"
#CELERY_RESULT_DBURI = "mysql://mydb_user:mydb_password@localhost/celery"

# BROKER_URL = 'message_broker://user:password@hostname:port/virtual_host'
# BROKER_URL = 'amqp://new_user:1q2w3e@localhost:5672/myvhost'
# BROKER_URL = 'redis:' #...
