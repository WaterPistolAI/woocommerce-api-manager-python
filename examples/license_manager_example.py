from wc_api_manager import LicenseManager

def main():
    url = 'https://yourstore.com'
    consumer_key = 'your_consumer_key'
    consumer_secret = 'your_consumer_secret'
    product_id = 'your_product_id'
    software_version = '1.0.0'
    api_key = 'your_api_key'
    instance = 'unique_instance_id'
    obj = 'activation_object'
    version = '1.0.0'
    plugin_name = 'your_plugin_name'

    license_manager_with_version = LicenseManager(f"{url}/wc-am-api", product_id, software_version)
    license_manager_without_version = LicenseManager(f"{url}/wc-am-api", product_id)

    # Activate the license
    activation_result_with_version = license_manager_with_version.activate(api_key, product_id, instance, obj, version)
    print('Activation result with version:', activation_result_with_version)

    activation_result_without_version = license_manager_without_version.activate(api_key, product_id, instance, obj, version)
    print('Activation result without version:', activation_result_without_version)

    # Check license status
    status_result_with_version = license_manager_with_version.status(api_key, product_id, instance, version)
    print('License status with version:', status_result_with_version)

    status_result_without_version = license_manager_without_version.status(api_key, product_id, instance, version)
    print('License status without version:', status_result_without_version)

    # Deactivate the license
    deactivation_result_with_version = license_manager_with_version.deactivate(api_key, product_id, instance)
    print('Deactivation result with version:', deactivation_result_with_version)

    deactivation_result_without_version = license_manager_without_version.deactivate(api_key, product_id, instance)
    print('Deactivation result without version:', deactivation_result_without_version)

    # Product list
    product_list_result = license_manager_with_version.product_list(api_key, instance)
    print('Product list:', product_list_result)

    # Verify API key is active
    verify_api_key_result = license_manager_with_version.verify_api_key_is_active(api_key)
    print('Verify API key is active:', verify_api_key_result)

    # Information
    information_result = license_manager_with_version.information(api_key, product_id, plugin_name, instance, version)
    print('Information:', information_result)

    # Update
    update_result = license_manager_with_version.update(api_key, product_id, plugin_name, instance, version)
    print('Update:', update_result)

if __name__ == '__main__':
    main()