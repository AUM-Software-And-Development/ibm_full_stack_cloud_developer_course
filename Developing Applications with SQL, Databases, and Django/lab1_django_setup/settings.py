from secrets import POSTGRES_PW

# Postgre SQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': POSTGRES_PW,
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

INSTALLED_APPS = (
    'orm',
)

SECRET_KEY = 'SECRET KEY for this Django Project'
