from pathlib import Path
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

ALLOWED_HOSTS = ['alfraganus-ntm.uz']
# ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'zokir-hal_alf',
        'USER': 'zokir-hal',
        'PASSWORD': '199403as',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
SECRET_KEY = '*9h$&ifjf*)ha0m4xr2*c(2p1hguc&ti7(--!@)s&)ga5hm40#'
DEBUG = True
