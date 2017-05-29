#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='slip_proactive',
    version='0.1.0',
    description="Proactive package for Slip",
    long_description=readme + '\n\n' + history,
    author="Stephen Fox",
    author_email='stephenfox995@hotmail.com',
    url='https://github.com/stephenfox1995/slip_proactive',
    packages=[
        'slip_proactive',
    ],
    package_dir={'slip_proactive':
                 'slip_proactive'},
    entry_points={
        'console_scripts': [
            'slip_proactive=slip_proactive.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='slip_proactive',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
