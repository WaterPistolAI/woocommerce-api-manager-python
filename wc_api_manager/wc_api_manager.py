from typing import Optional
import requests

class APIClient:
    """
    A client for making HTTP requests to a specified base URL.
    """
    def __init__(self, base_url: str):
        """
        Initializes the APIClient with a base URL.
        
        :param base_url: The base URL for the API.
        """
        self.base_url = base_url

    def get(self, endpoint: str, params: Optional[dict] = None):
        """
        Makes a GET request to the specified endpoint.
        
        :param endpoint: The endpoint to request.
        :param params: Optional parameters for the request.
        :return: The JSON response from the server.
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()

    def post(self, endpoint: str, data: dict, json_data: Optional[dict] = None):
        """
        Makes a POST request to the specified endpoint.
        
        :param endpoint: The endpoint to request.
        :param data: Data to be sent as form data.
        :param json_data: Optional JSON data to be sent.
        :return: The JSON response from the server.
        """
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, data=data, json=json_data)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()

class LicenseManager:
    """
    Manages license-related operations through an API.
    """
    def __init__(self, api_url: str, product_id: str, software_version: Optional[str] = None):
        """
        Initializes the LicenseManager.
        
        :param api_url: The URL of the license management API.
        :param product_id: The ID of the product.
        :param software_version: The version of the software.
        """
        self.api_url = api_url
        self.product_id = product_id
        self.software_version = software_version
        self.api_client = APIClient(api_url)

    def activate(self, api_key: str, product_id: str, instance: str, object: Optional[str], version: Optional[str]):
        """
        Activates a license.
        
        :param api_key: The API key for authentication.
        :param product_id: The product ID.
        :param instance: The instance identifier.
        :param object: The object being licensed.
        :param version: The version of the product.
        :return: The response from the API.
        """
        try:
            args = {
                'wc_am_action': 'activate',
                'api_key': api_key,
                'product_id': product_id,
                'instance': instance,
                'object': object,
                'version': version
            }
            return self.api_client.post('/wc-am-api', args)
        except requests.RequestException as e:
            # Handle the exception
            print(f"An error occurred: {e}")
            return None

    def deactivate(self, api_key: str, product_id: str, instance: str):
        """
        Deactivates a license.
        
        :param api_key: The API key for authentication.
        :param product_id: The product ID.
        :param instance: The instance identifier.
        :return: The response from the API.
        """
        try:
            args = {
                'wc_am_action': 'deactivate',
                'api_key': api_key,
                'product_id': product_id,
                'instance': instance
            }
            return self.api_client.post('/wc-am-api', args)
        except requests.RequestException as e:
            # Handle the exception
            print(f"An error occurred: {e}")
            return None

    def status(self, api_key: str, product_id: str, instance: str, version: Optional[str] = None):
        """
        Checks the status of a license.
        
        :param api_key: The API key for authentication.
        :param product_id: The product ID.
        :param instance: The instance identifier.
        :param version: The version of the product.
        :return: The response from the API.
        """
        try:
            args = {
                'wc_am_action': 'status',
                'api_key': api_key,
                'product_id': product_id,
                'instance': instance,
                'version': version
            }
            return self.api_client.post('/wc-am-api', args)
        except requests.RequestException as e:
            # Handle the exception
            print(f"An error occurred: {e}")
            return None

    def product_list(self, api_key: str, instance: str):
        """
        Retrieves a list of products.
        
        :param api_key: The API key for authentication.
        :param instance: The instance identifier.
        :return: The response from the API.
        """
        try:
            args = {
                'wc_am_action': 'product_list',
                'api_key': api_key,
                'instance': instance
            }
            return self.api_client.post('/wc-am-api', args)
        except requests.RequestException as e:
            # Handle the exception
            print(f"An error occurred: {e}")
            return None

    def verify_api_key_is_active(self, api_key: str):
        """
        Verifies if an API key is active.
        
        :param api_key: The API key to verify.
        :return: The response from the API.
        """
        try:
            args = {
                'wc_am_action': 'verify_api_key_is_active',
                'api_key': api_key
            }
            return self.api_client.post('/wc-am-api', args)
        except requests.RequestException as e:
            # Handle the exception
            print(f"An error occurred: {e}")
            return None

    def information(self, api_key: str, product_id: str, plugin_name: str, instance: str, version: Optional[str] = None):
        """
        Retrieves information about a product.
        
        :param api_key: The API key for authentication.
        :param product_id: The product ID.
        :param plugin_name: The name of the plugin.
        :param instance: The instance identifier.
        :param version: The version of the product.
        :return: The response from the API.
        """
        try:
            args = {
                'wc_am_action': 'information',
                'api_key': api_key,
                'product_id': product_id,
                'plugin_name': plugin_name,
                'instance': instance,
                'version': version
            }
            return self.api_client.post('/wc-am-api', args)
        except requests.RequestException as e:
            # Handle the exception
            print(f"An error occurred: {e}")
            return None

    def update(self, api_key: str, product_id: str, plugin_name: str, instance: str, version: str, slug: Optional[str] = None):
        """
        Updates a product.
        
        :param api_key: The API key for authentication.
        :param product_id: The product ID.
        :param plugin_name: The name of the plugin.
        :param instance: The instance identifier.
        :param version: The version of the product.
        :param slug: Optional slug for the update.
        :return: The response from the API.
        """
        try:
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
        except requests.RequestException as e:
            # Handle the exception
            print(f"An error occurred: {e}")
            return None