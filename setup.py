from setuptools import setup, find_packages

setup(
    name='wc-api-manager',
    version='0.1.0',
    description='Python Library for WooCommerce Kestrel API Manager',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Devin J. Dawson',
    author_email='devin@waterpistol.co',
    url='https://github.com/unclemusclez/wc-api-manager-python',
    packages=find_packages(),
    install_requires=[
        'requests',
        'typing'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)