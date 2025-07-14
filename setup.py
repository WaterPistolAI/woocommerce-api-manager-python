from setuptools import setup, find_packages
import pprint

packages = find_packages()
print("Found packages:")
pprint.pprint(packages)
setup(
    name='woocommerce-api-manager',
    version='0.5.0',
    description='Python Library for WooCommerce Kestrel API Manager',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Devin J. Dawson',
    author_email='devin@waterpistol.co',
    url='https://github.com/unclemusclez/wc-api-manager-python',
    packages=packages,
    install_requires=[
        'woocommerce'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    license='MIT',
    python_requires='>=3.6',
)