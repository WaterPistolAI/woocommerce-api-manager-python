from typing import Optional
import requests

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get(self, endpoint: str, params: Optional[dict] = None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()

    def post(self, endpoint: str, data: dict):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, data=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()

class LicenseManager:
    def __init__(self, api_url: str, product_id: str, software_version: str):
        self.api_url = api_url
        self.product_id = product_id
        self.software_version = software_version
        self.api_client = APIClient(api_url)

    def activate(self, api_key: str, product_id: str, instance: str, object: str, version: str):
        args = {
            'wc_am_action': 'activate',
            'api_key': api_key,
            'product_id': product_id,
            'instance': instance,
            'object': object,
            'version': version
        }
        return self.api_client.post('/wc-am-api', args)

    def deactivate(self, api_key: str, product_id: str, instance: str):
        args = {
            'wc_am_action': 'deactivate',
            'api_key': api_key,
            'product_id': product_id,
            'instance': instance
        }
        return self.api_client.post('/wc-am-api', args)

    def status(self, api_key: str, product_id: str, instance: str, version: str):
        args = {
            'wc_am_action': 'status',
            'api_key': api_key,
            'product_id': product_id,
            'instance': instance,
            'version': version
        }
        return self.api_client.post('/wc-am-api', args)

    def product_list(self, api_key: str, instance: str):
        args = {
            'wc_am_action': 'product_list',
            'api_key': api_key,
            'instance': instance
        }
        return self.api_client.post('/wc-am-api', args)

    def verify_api_key_is_active(self, api_key: str):
        args = {
            'wc_am_action': 'verify_api_key_is_active',
            'api_key': api_key
        }
        return self.api_client.post('/wc-am-api', args)

    def information(self, api_key: str, product_id: str, plugin_name: str, instance: str, version: str):
        args = {
            'wc_am_action': 'information',
            'api_key': api_key,
            'product_id': product_id,
            'plugin_name': plugin_name,
            'instance': instance,
            'version': version
        }
        return self.api_client.post('/wc-am-api', args)

    def update(self, api_key: str, product_id: str, plugin_name: str, instance: str, version: str, slug: Optional[str] = None):
        args = {
            'wc_am_action': 'update',
            'api_key': api_key,
            'product_id': product_id,
            'plugin_name': plugin_name,
            'instance': instance,
            'version': version
        }
        if slug:
            args['slug'] = slug
        return self.api_client.post('/wc-am-api', args)