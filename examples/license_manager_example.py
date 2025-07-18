import os
import logging
from woocommerce_api_manager import APIManager
from dotenv import load_dotenv

load_dotenv()

def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    # Load environment variables
    url = os.getenv('WC_URL', '')
    product_id = os.getenv('WC_PRODUCT_ID', 0)
    api_key = os.getenv('WCAM_API_KEY', '')
    instance = os.getenv('WCAM_INSTANCE','')
    obj = os.getenv('WCAM_OBJ', None)
    product_version = os.getenv('WCAM_PRODUCT_VERSION', '')
    product_name = os.getenv('WCAM_PRODUCT_NAME', '')

    # Validate environment variables
    required_env_vars = [url, api_key, instance, obj, product_name ]
    if not all(required_env_vars):
        raise ValueError("Missing required environment variables")

    url, api_key, instance, obj, product_name = [str(var) for var in required_env_vars]

    try:
        product_id = int(product_id)
        logger.info(f"Product ID: {product_id}")
    except ValueError:
        logger.error("WC_PRODUCT_ID must be a valid integer")
        raise ValueError("WC_PRODUCT_ID must be a valid integer")

    # Instantiate APIManager
    license_manager = APIManager(url)
    
    # Deactivate the license
    deactivation_result = license_manager.deactivate(api_key, product_id, instance)
    if deactivation_result is not None:
        logger.info('Deactivation result: %s', deactivation_result)
        logger.info('Deactivation result JSON: %s', deactivation_result.json())
    else:
        logger.info('Deactivation failed: No response received')
        
    # Activate the license
    activation_result = license_manager.activate(api_key, product_id, instance, obj, product_version)
    if activation_result is not None:
        logger.info('Activation result: %s', activation_result)
        logger.info('Activation result JSON: %s', activation_result.json())
    else:
        logger.info('Activation failed: No response received')

    # Check license status
    status_result = license_manager.status(api_key, product_id, instance)
    if status_result is not None:
        logger.info('License status: %s', status_result)
        logger.info('License status JSON: %s', status_result.json())
    else:
        logger.info('Failed to retrieve license status')
        
    ##
    # Note: If the return value for status_check is active, or for activated is true,
    # then the time limit has not expired and the API Key is still active. 
    # If this is for a subscription, then the subscription is still active. 
    # The API Manager verifies the API Key activation should still exists, 
    # and deletes it if it should not, due to an expired time limit or inactive subscription, 
    # before returning a response.
    ##


    # Product list
    product_list_result = license_manager.product_list(api_key, instance)
    if product_list_result is not None:
        logger.info('Product list: %s', product_list_result)
        logger.info('Product list JSON: %s', product_list_result.json())
    else:
        logger.info('Failed to retrieve product list')

    # Verify API key is active
    verify_api_key_result = license_manager.verify_api_key_is_active(api_key)
    if verify_api_key_result is not None:
        logger.info('Verify API key is active: %s', verify_api_key_result)
        logger.info('Verify API key is active JSON: %s', verify_api_key_result.json())
    else:
        logger.info('Failed to verify API key status')
        
    # Information
    information_result = license_manager.information(product_id, product_name)
    if information_result is not None:
        logger.info('Information: %s', information_result)
        logger.info('Information JSON: %s', information_result.json())
    else:
        logger.info('Failed to retrieve information')

    # Information
    authenticated_information_result = license_manager.authenticated_information(api_key, product_id, product_name, instance, product_version)
    if authenticated_information_result is not None:
        logger.info('Authenticated Information: %s', authenticated_information_result)
        logger.info('Authenticated Information JSON: %s', authenticated_information_result.json())
    else:
        logger.info('Failed to retrieve information')

    # Update
    update_result = license_manager.update(api_key, product_id, product_name, instance, product_version)
    if update_result is not None:
        logger.info('Update: %s', update_result)
        logger.info('Update JSON: %s', update_result.json())
    else:
        logger.info('Failed to perform update')

if __name__ == '__main__':
    main() 