SECRET_KEY = 'dummykey'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = ['django.contrib.staticfiles', 'tracker']
MIDDLEWARE = ['django.middleware.common.CommonMiddleware']
ROOT_URLCONF = 'project.urls'
TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {},
}]
WSGI_APPLICATION = 'project.wsgi.application'
DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': 'db.sqlite3'}}
STATIC_URL = '/static/'
