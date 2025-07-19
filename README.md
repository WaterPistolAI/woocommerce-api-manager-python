# WooCommerce Kestrel API Manager Python Library

A Python library for interacting with the WooCommerce Kestrel API Manager, providing easy integration and simplified API calls.

## Features

* Easy integration with WooCommerce Kestrel API Manager
* Simplified API calls

## Installation

To install the WooCommerce Kestrel API Manager Python Library, run the following command:

```bash
pip install git+https://github.com/unclemusclez/wc-api-manager-python
```

## Usage Examples

### Basic Usage

Here's a simple example of how to use the library:

```python
from woocommerce_api_manager import APIKeyManager

# Initialize the API manager
api_manager = APIKeyManager(your_api_url, your_consumer_key, your_consumer_secret)

# Make an API call
response = api_manager.get('products')

# Print the response
print(response.json())
```

### License Manager Example

For more advanced usage, you can utilize the `APIKeyManager` class to manage licenses:

```python
import os
from woocommerce_api_manager import APIKeyManager
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
url = os.getenv('WC_URL', '')
product_id = int(os.getenv('WC_PRODUCT_ID', 0))
api_key = os.getenv('WCAM_API_KEY', '')
instance = os.getenv('WCAM_INSTANCE', '')
obj = os.getenv('WCAM_OBJ', None)
product_version = os.getenv('WCAM_PRODUCT_VERSION', '')
product_name = os.getenv('WCAM_PRODUCT_NAME', '')

# Instantiate APIKeyManager
license_manager = APIKeyManager(url)

# Deactivate the license
deactivation_result = license_manager.deactivate(api_key, product_id, instance)

# Activate the license
activation_result = license_manager.activate(api_key, product_id, instance, obj, product_version)

# Check license status
status_result = license_manager.status(api_key, product_id, instance)

# Product list
product_list_result = license_manager.product_list(api_key, instance)

# Verify API key is active
verify_api_key_result = license_manager.verify_api_key_is_active(api_key)

# Information
information_result = license_manager.information(product_id, product_name)

# Authenticated Information
authenticated_information_result = license_manager.authenticated_information(api_key, product_id, product_name, instance, product_version)

# Update
update_result = license_manager.update(api_key, product_id, product_name, instance, product_version)
```

This example demonstrates how to use the `APIKeyManager` class for various license management operations.

## Documentation

For more information, please refer to the [WooCommerce Kestrel API Manager Documentation](https://woocommerce.com/document/api-documentation).

## Woocommerce Plugin Page

Visit the [Woocommerce Plugin Page](https://woocommerce.com/products/woocommerce-api-manager/) for more details about the plugin.
