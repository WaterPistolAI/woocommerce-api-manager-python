import os
from woocommerce_api_manager import LicenseManager
from dotenv import load_dotenv

load_dotenv()

def main():
    # Load environment variables
    url = os.getenv('WC_URL', '')
    product_id = os.getenv('WC_PRODUCT_ID', 0)
    api_key = os.getenv('WCAM_API_KEY', '')
    instance = os.getenv('WCAM_INSTANCE','')
    obj = os.getenv('WCAM_OBJ', '')
    version = os.getenv('WCAM_VERSION', '')
    plugin_name = os.getenv('WCAM_PLUGIN_NAME', '')

    # Validate environment variables
    required_env_vars = [url, api_key, instance, obj, plugin_name]
    if not all(required_env_vars):
        raise ValueError("Missing required environment variables")

    url, api_key, instance, obj, plugin_name = [str(var) for var in required_env_vars]
    
    try:
        product_id = int(product_id)
    except ValueError:
        raise ValueError("WC_PRODUCT_ID must be a valid integer")


    # Instantiate LicenseManager
    license_manager_with_version = LicenseManager(url)

    # Activate the license
    activation_result_with_version = license_manager_with_version.activate(api_key,instance, product_id,  obj, version)
    print('Activation result with version:', activation_result_with_version)

    # Check license status
    status_result_with_version = license_manager_with_version.status(api_key, instance, product_id, version)
    print('License status with version:', status_result_with_version)

    # Deactivate the license
    deactivation_result_with_version = license_manager_with_version.deactivate(api_key, instance, product_id )
    print('Deactivation result with version:', deactivation_result_with_version)

    # Product list
    product_list_result = license_manager_with_version.product_list(api_key, instance)
    print('Product list:', product_list_result)

    # Verify API key is active
    verify_api_key_result = license_manager_with_version.verify_api_key_is_active(api_key)
    print('Verify API key is active:', verify_api_key_result)

    # Information
    information_result = license_manager_with_version.information(api_key, instance, product_id, plugin_name, version)
    print('Information:', information_result)

    # Update
    update_result = license_manager_with_version.update(api_key, instance, product_id, plugin_name, version)
    print('Update:', update_result)

if __name__ == '__main__':
    main()