import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='djangorestframework-docjson',
    version='0.0.4',
    packages=['rest_framework_docjson'],
    include_package_data=True,
    license='BSD License',
    description='Some helper classes for Django Rest Framework for building hypermedia APIs with the DocJSON document format.',
    long_description=README,
    author='Michael Paulus',
    author_email='mdpaulus@gmail.com',
    install_requires=['djangorestframework'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
