
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '../../res/raw/pokedex_db',                      # Or path to database file if using sqlite3.
    }
}
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    "south",
    "app",
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ekmfjecg*56#039+y=)8)n=b02i0=!s$ty28oxlrtd$y^d%08='
