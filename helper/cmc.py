
from config import Config
import requests
from models import RawMetadataFeedModel
from tasks.metadata import insert_metadata
from web3 import Web3
from lib.logger import debug
import traceback

headers = {
    'X-CMC_PRO_API_KEY': Config.CMC_API_TOKEN,
    'Accept': '*/*'

}
base_url = Config.CMC_API_URL

class CmcHelperService:
    
  
    @staticmethod
    def get_metadata(form_data=None):
        try:
            _params_filter, _params = {}, {}
            if "id" in form_data:
                _params = {
                "id": form_data['id']  
                }
                
                _params_filter =  {
                **_params_filter,
                "metadata.id": int(form_data['id'])  
                }
                
            if "slug" in form_data:
                _params = {
                "slug": form_data['slug']  
                }
                
                _params_filter =  {
                **_params_filter,
                "metadata.slug": form_data['slug']
                }
                 

            if "address"  in form_data:
                form_data['address'] = Web3.toChecksumAddress(form_data['address']) 

                _params = {
                **_params,
                "address": form_data['address']  
                } 
                _params_filter =  {
                **_params_filter,
                # "metadata.contract_address.contract_address": form_data['address']  ,
                "contract_address": {"$elemMatch": {"contract_address":  { "$regex" : f"{form_data['address']}",  "$options": 'i'   }}}
                }   

            # Check existing project metadata
            print("_params_filter ", _params_filter)
            _data = RawMetadataFeedModel.find_one(filter=_params_filter)

            if _data:
                return _data['metadata']
            else:    
                # Get from API
                response = requests.get(base_url + '/cryptocurrency/info', params=_params, headers=headers)
                response_data = response.json()
                if 'data' not in response_data:
                    return {}
                
                _data =  response_data['data']    
                if len(_data) == 1:
                    for item in _data:
                        _data =  _data[item]
                            
                insert_metadata.delay(_data)

                return _data
        except Exception:
            debug(traceback.format_exc())
            return {}
        