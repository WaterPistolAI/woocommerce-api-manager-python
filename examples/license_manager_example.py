import os
from woocommerce_api_manager import LicenseManager
from dotenv import load_dotenv

load_dotenv()

def main():
    # Load environment variables
    url = os.getenv('WC_URL')
    consumer_key = os.getenv('WC_CONSUMER_KEY')
    consumer_secret = os.getenv('WC_CONSUMER_SECRET')
    product_id = os.getenv('WC_PRODUCT_ID')
    software_version = os.getenv('WCAM_SOFTWARE_VERSION')
    api_key = os.getenv('WCAM_API_KEY')
    instance = os.getenv('WCAM_INSTANCE')
    obj = os.getenv('WCAM_OBJ')
    version = os.getenv('WCAM_VERSION')
    plugin_name = os.getenv('WCAM_PLUGIN_NAME')

    # Validate environment variables
    required_env_vars = [url, api_key, instance, obj, version, plugin_name]
    if not all(required_env_vars):
        raise ValueError("Missing required environment variables")
    
    # Convert product_id to int if it exists
    product_id = int(product_id) if product_id else None

    url, api_key, instance, obj, version, plugin_name = [str(var) for var in required_env_vars]
    software_version = str(software_version) if software_version else None

    # Instantiate LicenseManager
    license_manager_with_version = LicenseManager(url, product_id, software_version=software_version)
    license_manager_without_version = LicenseManager(url, product_id)

    # Activate the license
    activation_result_with_version = license_manager_with_version.activate(api_key, str(product_id), instance, obj, version)
    print('Activation result with version:', activation_result_with_version)

    activation_result_without_version = license_manager_without_version.activate(api_key, str(product_id), instance, obj, version)
    print('Activation result without version:', activation_result_without_version)

    # Check license status
    status_result_with_version = license_manager_with_version.status(api_key, str(product_id), instance, version)
    print('License status with version:', status_result_with_version)

    status_result_without_version = license_manager_without_version.status(api_key, str(product_id), instance, version)
    print('License status without version:', status_result_without_version)

    # Deactivate the license
    deactivation_result_with_version = license_manager_with_version.deactivate(api_key, str(product_id), instance)
    print('Deactivation result with version:', deactivation_result_with_version)

    deactivation_result_without_version = license_manager_without_version.deactivate(api_key, str(product_id), instance)
    print('Deactivation result without version:', deactivation_result_without_version)

    # Product list
    product_list_result = license_manager_with_version.product_list(api_key, instance)
    print('Product list:', product_list_result)

    # Verify API key is active
    verify_api_key_result = license_manager_with_version.verify_api_key_is_active(api_key)
    print('Verify API key is active:', verify_api_key_result)

    # Information
    information_result = license_manager_with_version.information(api_key, str(product_id), plugin_name, instance, version)
    print('Information:', information_result)

    # Update
    update_result = license_manager_with_version.update(api_key, str(product_id), plugin_name, instance, version)
    print('Update:', update_result)

if __name__ == '__main__':
    main()