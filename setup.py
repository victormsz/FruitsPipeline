from setuptools import setup, find_packages

setup(
    name='avaliar_fruta',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Victor',
    description='Um projeto que avalia frutas pela proteína',
)