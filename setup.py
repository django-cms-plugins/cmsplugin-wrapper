from setuptools import setup, find_packages
import os

import packit

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
    name='django-packit',
    version=packit.get_version(),
    description='Generic app to calculate packages fitting into bin(s) ',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Oyvind Saltvik',
    author_email='oyvind.saltvik@gmail.com',
    url='http://github.com/fivethreeo/django-packit/',
    packages=find_packages(),
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False,
    install_requires=['Django']
)
