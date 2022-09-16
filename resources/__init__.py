# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from resources.health_check import HealthCheck
from resources.metadata import MetadataResource
from resources.iapi import iapi_resources

api_resources = {
    '/query': MetadataResource,
    '/common/health_check': HealthCheck,
    **{f'/iapi{k}': val for k, val in iapi_resources.items()}
}
