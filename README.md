# WC API Manager Python Library

A Python library for interacting with the WC API Manager, providing easy integration and simplified API calls.

## Features

* Easy integration with WC API Manager
* Simplified API calls

## Installation

To install the WC API Manager Python Library, run the following command:

```bash
pip install git+https://github.com/unclemusclez/wc-api-manager-python
```

## Usage Example

Here's a simple example of how to use the library:

```python
from wc_api_manager import WC_API_Manager

# Initialize the API manager
api_manager = WC_API_Manager(your_api_url, your_consumer_key, your_consumer_secret)

# Make an API call
response = api_manager.get('products')

# Print the response
print(response.json())
```

## Documentation

For more information, please refer to the [WC API Manager Documentation](https://woocommerce.com/document/api-documentation).

## Woocommerce Plugin Page

Visit the [Woocommerce Plugin Page](https://woocommerce.com/products/woocommerce-api-manager/) for more details about the plugin.
