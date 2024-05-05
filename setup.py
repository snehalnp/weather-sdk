from setuptools import setup, find_packages

setup(
    name="weather-sdk",
    version="0.1",
    packages=find_packages(),
    install_requires=["requests"],
    author="Snehal Palve",
    description="A simple SDK for interacting with the OpenWeatherMap API",
    url="https://github.com/snehalnp/weather-sdk",
)
