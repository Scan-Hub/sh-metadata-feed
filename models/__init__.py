# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from config import Config
from lib import DaoModel, AsyncDaoModel
from connect import connect_db, redis_cluster, asyncio_mongo

__models__ = ['']

from models.user import UserDao

UserModel = UserDao(connect_db.db.users, redis=redis_cluster) # broker for write db with queue

RawMetadataFeedModel = UserDao(connect_db.db.raw_metadata_feed, redis=redis_cluster) 

