from setuptools import setup, find_packages

setup(
    name='weather_sdk',
    version='0.1',
    packages=find_packages(),
    package_dir={'': '.'},
    install_requires=[
        'requests',
    ],
)
