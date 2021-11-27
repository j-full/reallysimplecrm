# reallysimplecrm

###### to settings.py:
```
from django.contrib.messages import constants as messages

INSTALLED_APPS = [
  
    'widget_tweaks',
    'accounts',
    'crm',
    'basicpages',
    'openpyxl',
]

TEMPLATES = [
    {
        'DIRS': [
            BASE_DIR / 'templates/',
        ],
        'APP_DIRS': True,
    },
]


AUTH_USER_MODEL = 'accounts.User'


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / 'media'


LOGOUT_REDIRECT_URL = 'home'
LOGIN_REDIRECT_URL = 'dashboard'

MESSAGE_TAGS = {
    messages.SUCCESS: 'alert-success',
}
```

