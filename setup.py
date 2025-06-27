from setuptools import setup, find_packages

setup(
    name="adsnap_studio",
    version="0.1.0",
    packages=find_packages(include=["components", "services", "utils", "workflows"]),
    install_requires=open("requirements.txt").read().splitlines(),
)