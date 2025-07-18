from typing import Optional
from woocommerce import API

class LicenseManager:
    """
    Manages license-related operations through the WooCommerce API Manager.
    """
    
    def __init__(self, url: str):

        """
        Initializes the LicenseManager.
        
        :param url: The URL of the WooCommerce store (e.g., https://yourstore.com).
        # :param consumer_key: The consumer key for the WooCommerce API.
        # :param consumer_secret: The consumer secret for the WooCommerce API.
        # :param product_id: The ID of the product.
        # :param software_version: The version of the software.
        """
        self.wcapi = API(
            url=url,
            consumer_key='',
            consumer_secret='',
            wp_api=False,
            version="wc-am-api",
        )
        self.endpoint=''

    def _handle_response(self, response):
        """Parse API response and return JSON dict or None on failure."""
        try:
            if response.status_code != 200:
                print(f"HTTP error: {response.status_code} - {response.text}")
                return None
            return response
        except Exception as e:
            print(f"Error parsing response: {e}")
            return None

    def activate(self, api_key: str, product_id: int, instance: str, object: Optional[str] = None, version: Optional[str] = None):
        """
        Activates a license.
        
        :param api_key: The API key for authentication.
        :param product_id: The product ID (defaults to self.product_id if None).
        :param instance: The instance identifier.
        :param object: The object being licensed.
        :param version: The version of the product.
        :return: Parsed JSON response dict or None on failure.
        """
        args = {
            'wc_am_action': 'activate',
            'api_key': api_key,
            'instance': instance,
            'product_id': product_id,
            'object': object,
            'version': version 
        }
        # print(f"Activate args: {args}")
        response = self.wcapi.get(self.endpoint, params=args)
        return self._handle_response(response)

    def deactivate(self, api_key: str, product_id: int, instance: str):
        """
        Deactivates a license.
        
        :param api_key: The API key for authentication.
        :param product_id: The product ID.
        :param instance: The instance identifier.
        :return: Parsed JSON response dict or None on failure.
        """
        args = {
            'wc_am_action': 'deactivate',
            'api_key': api_key,
            'product_id': product_id,
            'instance': instance

        }
        # print(f"Deactivate args: {args}")
        response = self.wcapi.get(self.endpoint, params=args)
        return self._handle_response(response)

    def status(self, api_key: str, product_id: int, instance: str, version: Optional[str] = None):
        """
        Checks the status of a license.
        
        :param api_key: The API key for authentication.
        :param product_id: The product ID.
        :param instance: The instance identifier.
        :param version: The version of the product.
        :return: Parsed JSON response dict or None on failure.
        """
        args = {
            'wc_am_action': 'status',
            'api_key': api_key,
            'product_id': product_id,
            'instance': instance,
            'version': version
        }
        # print(f"Status args: {args}")
        response = self.wcapi.get(self.endpoint, params=args)
        return self._handle_response(response)

    def product_list(self, api_key: str, instance: str):
        """
        Retrieves a list of products.
        
        :param api_key: The API key for authentication.
        :param instance: The instance identifier.
        :return: Parsed JSON response dict or None on failure.
        """
        args = {
            'wc_am_action': 'product_list',
            'api_key': api_key,
            'instance': instance
        }
        # print(f"Product list args: {args}")
        response = self.wcapi.get(self.endpoint, params=args)
        return self._handle_response(response)

    def verify_api_key_is_active(self, api_key: str):
        """
        Verifies if an API key is active.
        
        :param api_key: The API key to verify.
        :return: Parsed JSON response dict or None on failure.
        """
        args = {
            'wc_am_action': 'verify_api_key_is_active',
            'api_key': api_key
        }
        # print(f"Verify API key args: {args}")
        response = self.wcapi.get(self.endpoint, params=args)
        return self._handle_response(response)

    def information(self, product_id: int, plugin_name: str):
        """
        Retrieves information about a product.
        
        :param product_id: The product ID.
        :param plugin_name: The name of the plugin.
        :return: Parsed JSON response dict or None on failure.
        """
        args = {
            'wc_am_action': 'information',
            'product_id': product_id,
            'plugin_name': plugin_name
        }
        # print(f"Information args: {args}")
        # print(f"Update args: {args}")
        response = self.wcapi.get(self.endpoint, params=args)
        return self._handle_response(response)
    
    def authenticated_information(self, api_key: str, product_id: int, plugin_name: str, instance: str, version: str):
        """
        Retrieves information about a product.
        
        :param api_key: The API key for authentication.
        :param product_id: The product ID.
        :param instance: The instance identifier.
        :param plugin_name: The name of the plugin.
        :param version: The version of the product.
        :return: Parsed JSON response dict or None on failure.
        """
        args = {
            'wc_am_action': 'information',
            'api_key': api_key,
            'product_id': product_id,
            'instance': instance,
            'plugin_name': plugin_name,
            'version': version
        }
        # print(f"Information args: {args}")
        # print(f"Update args: {args}")
        response = self.wcapi.get(self.endpoint, params=args)
        return self._handle_response(response)


    def update(self, api_key: str, product_id: int, plugin_name: str, instance: str, version: str, slug: Optional[str] = None):
        """
        Updates a product.
        
        :param api_key: The API key for authentication.
        :param product_id: The product ID.
        :param instance: The instance identifier.
        :param plugin_name: The name of the plugin.
        :param version: The version of the product.
        :param slug: Optional slug for the update.
        :return: Parsed JSON response dict or None on failure.
        """
        args = {
            'wc_am_action': 'update',
            'api_key': api_key,
            'product_id': product_id,
            'instance': instance,
            'plugin_name': plugin_name,
            'version': version
        }
        if slug:
            args['slug'] = slug
        response = self.wcapi.get(self.endpoint, params=args)
        return self._handle_response(response)