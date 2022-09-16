# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask_restful import Resource

from models import UserModel
from schemas.hello import HelloSchema
from connect import security
from helper.cmc import CmcHelperService
from flask import Flask, request

class MetadataResource(Resource):

    @security.http(
        login_required=False
    )
    def get(self):
        form_data = request.args.to_dict()
       
        _result = CmcHelperService.get_metadata(form_data)
        return _result

