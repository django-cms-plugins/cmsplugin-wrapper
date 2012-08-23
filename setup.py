from setuptools import setup, find_packages
import os

import cmsplugin_wrapper

CLASSIFIERS = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
]

setup(
    name='cmsplugin-wrapper',
    version=cmsplugin_wrapper.get_version(),
    description='A plugin to wrap other plugins in django-cms',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Oyvind Saltvik',
    author_email='oyvind.saltvik@gmail.com',
    url='http://github.com/fivethreeo/cmsplugin-wrapper/',
    packages=find_packages(),
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False,
    install_requires=['Django']
)
