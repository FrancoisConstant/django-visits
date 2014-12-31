import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-visits',
    version='0.1',
    packages=['visits'],
    include_package_data=True,
    license='MIT License',
    description='A simple Django app to save the number of visits on any Django Model.',
    long_description=README,
    url='https://github.com/FrancoisConstant/django-visits',
    author='Francois Constant',
    author_email='francois.constant@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)