# -----------------------------------------------------------------------------
# PantryPy
# Copyright (c) 2023 Felipe Amaral dos Santos
# Licensed under the MIT License (see LICENSE file)
# -----------------------------------------------------------------------------

from setuptools import setup, find_packages


setup(
    name='PantryPy',
    version='1.0.1a5',
    description='PantryPy is a Python library for enhanced typing with custom annotations',
    author='Felipe Amaral',
    author_email='lipeamaralsantos@gmail.com',
    url='https://github.com/Feliperaxd/pantrypy.git',
    license='MIT',
    keywords='PantryPy pantry py type typing',
    packages=find_packages(),
    install_requires=['colorama==0.4.4']
)
