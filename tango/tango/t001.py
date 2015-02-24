__author__ = 'Anne'
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates').replace('\\','/')
STATIC_URL = '/static/'
STATIC_PATH = os.path.join(BASE_DIR,'static').replace('\\','/')

#STATIC_URL = '/static/' # You may find this is already defined as such.

STATICFILES_DIRS = (
    STATIC_PATH,
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\','/') # Absolute path

print TEMPLATE_PATH,STATICFILES_DIRS,MEDIA_ROOT