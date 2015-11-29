from codecs import open
from os import path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ascribe',
    version='0.0.7.dev1',
    description='ascribe api',
    long_description=long_description,
    url='https://ascribe.readthedocs.org',
    author='Oskar Paolini, Sylvain Bellemare',
    author_email='sylvain@ascribe.io',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords=(
        'intellectual property, attribution, ownership, art, blockchain, api '
        'digital work, provenance, spool'
    ),

    py_modules=["ascribe"],

    install_requires=['requests'],

    extras_require={
        'test': ['coverage', 'pytest'],
    },
)
