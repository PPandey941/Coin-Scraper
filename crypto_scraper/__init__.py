# crypto_scraper/__init__.py
from __future__ import absolute_import, unicode_literals

# crypto_scraper/crypto_scraper/__init__.py

from .celery import app as celery_app

__all__ = ('celery_app',)
