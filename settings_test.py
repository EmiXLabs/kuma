from settings import INSTALLED_APPS

CELERY_ALWAYS_EAGER = True
ES_LIVE_INDEX = False
ES_URLS = ['localhost:9200']

INSTALLED_APPS += (
    'kuma.core.tests.taggit_extras',
    'kuma.actioncounters.tests',
)
