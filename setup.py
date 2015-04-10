import sys
from setuptools import setup, find_packages

'''
packaging modeled after
https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
'''


def read(filename):
    return open(filename).read()

setup(
    name='vultr',
    version='0.1.0',
    install_requires=[
      "requests"
    ],
    description='Vultr.com API Client',
    long_description=(read('README.rst')),
    url='http://github.com/spry-group/python-vultr',
    author='Darrel O\'Pry',
    author_email='darrel.opry@spry-group.com',
    packages=['vultr'],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    license=read('LICENSE'),
    test_suite='tests'
)
