# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
import json
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    DEBUG = False
    PROJECT = "micro-api"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    SENTRY_DSN = os.getenv('SENTRY_DSN')
    # Setup db
    MONGO_URI = os.getenv('MONGO_URI')
    # Authentication
    AUTH_ADDRESS = os.getenv('AUTH_ADDRESS')

    CELERY_IMPORTS = ['tasks']
    ENABLE_UTC = True

    # Config celery worker

    BROKER_URL = os.getenv('BROKER_URL')
    CELERY_QUEUES = os.getenv('CELERY_QUEUES')
    DEFAULT_QUEUE = 'sh-metadata-feed-queue'
    
    CELERY_ROUTES = {
        'worker.task_insert_metadata': {'queue': DEFAULT_QUEUE}
    }
    PUBLIC_PATH = os.getenv('PUBLIC_PATH')
    REDIS_CLUSTER = json.loads(os.getenv('REDIS_CLUSTER'))
    
    
    # CMC config
    CMC_API_TOKEN = os.getenv('CMC_API_TOKEN')
    CMC_API_URL = os.getenv('CMC_API_URL')

