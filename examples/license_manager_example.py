from wc_api_manager import LicenseManager

def main():
    api_url = 'https://api.example.com'
    product_id = 'your_product_id'
    software_version = '1.0.0'
    api_key = 'your_api_key'
    instance = 'unique_instance_id'
    object = 'activation_object'
    version = '1.0.0'

    # software_version is optional
    license_manager = LicenseManager(api_url, product_id, software_version)
    # Alternatively, you can omit software_version
    # license_manager = LicenseManager(api_url, product_id)

    # Activate the license
    activation_result = license_manager.activate(api_key, product_id, instance, object, version)
    print('Activation result:', activation_result)

    # Check license status
    status_result = license_manager.status(api_key, product_id, instance, version)
    print('License status:', status_result)

    # Deactivate the license
    deactivation_result = license_manager.deactivate(api_key, product_id, instance)
    print('Deactivation result:', deactivation_result)

if __name__ == '__main__':
    main()