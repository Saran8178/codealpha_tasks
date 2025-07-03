SECRET_KEY = 'dummykey'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = ['django.contrib.staticfiles', 'store']
MIDDLEWARE = ['django.middleware.common.CommonMiddleware']
ROOT_URLCONF = 'ecommerce.urls'
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {},
}]
WSGI_APPLICATION = 'ecommerce.wsgi.application'
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'db.sqlite3'}}
STATIC_URL = '/static/'
