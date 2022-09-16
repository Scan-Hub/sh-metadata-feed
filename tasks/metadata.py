# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from worker import worker
from models import RawMetadataFeedModel


@worker.task(name='worker.task_insert_metadata', rate_limit='1000/s')
def insert_metadata(metadata):

    _data_insert = {
        'created_by':  'api' ,
        'source': 'CMC',
        'contract_address': metadata["contract_address"],
        'metadata': metadata
    } 
    
    RawMetadataFeedModel.insert_one(_data_insert)
        
    

