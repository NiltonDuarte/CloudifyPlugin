from setuptools import setup

setup(
    name='my-plugin',
    version='0.0',
    author='Cloudify',
    packages=['my_plugin'],
    install_requires=['cloudify-plugins-common>=3.3'],
)