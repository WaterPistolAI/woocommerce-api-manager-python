import os
import json
from woocommerce_api_manager import LicenseManager
from dotenv import load_dotenv

load_dotenv()

def main():
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
        print(f"Product ID:{product_id}")
    except ValueError:
        raise ValueError("WC_PRODUCT_ID must be a valid integer")

    # product_name = ''
    # product_name = ''
    # product_version = ''


    # Instantiate LicenseManager
    license_manager = LicenseManager(url)

    # Activate the license
    activation_result = license_manager.activate(api_key, product_id, instance, obj, product_version)
    
    if activation_result is not None:
        print('Activation result:', activation_result)
        print('Text result:', activation_result.text)
        # print('Status Code result:', activation_result.status_code)
        # print('Activation result JSON:', activation_result.json)
        # if activation_result.error:
        #     print('Activation result JSON:', activation_result.error)
        
    else:
        print('Activation failed: No response received')

    # Check license status
    status_result = license_manager.status(api_key, product_id, instance)
    if status_result is not None:
        print('License status:', status_result)
    else:
        print('Failed to retrieve license status')

    # Deactivate the license
    deactivation_result = license_manager.deactivate(api_key, product_id, instance)
    if deactivation_result is not None:
        print('Deactivation result:', deactivation_result)
        print('Deactivation result:', deactivation_result.text)
    else:
        print('Deactivation failed: No response received')

    # Product list
    product_list_result = license_manager.product_list(api_key, instance)
    if product_list_result is not None:
        print('Product list:', product_list_result)
        print('Product list:', product_list_result.text)
    else:
        print('Failed to retrieve product list')

    # Verify API key is active
    verify_api_key_result = license_manager.verify_api_key_is_active(api_key)
    if verify_api_key_result is not None:
        print('Verify API key is active:', verify_api_key_result)
        print('Verify API key is active:', verify_api_key_result.text)
    else:
        print('Failed to verify API key status')

    # Information
    information_result = license_manager.information(api_key, product_id, instance,  product_name)
    if information_result is not None:
        print('Information:', information_result)
        print('Information:', information_result.text)
    else:
        print('Failed to retrieve information')

    # Update
    update_result = license_manager.update(api_key, product_id, instance,  product_name, product_version)
    if update_result is not None:
        print('Update:', update_result)
    else:
        print('Failed to perform update')

if __name__ == '__main__':
    main() 