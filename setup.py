#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

import setuptools

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = ['Click>=6.0', 'GitPython>=2.1.11']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setuptools.setup(
    author="Martin Skarzynski",
    author_email='marskar@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Combine multiple git version controls steps into one.",
    entry_points={
        'console_scripts': [
            'cam=cli.cam_cli:cam_cli',
            'camp=cli.camp_cli:camp_cli',
            'acm=cli.acm_cli:acm_cli',
            'acmp=cli.acmp_cli:acmp_cli',
            'amend=cli.amend_cli:amend_cli',
            'amendp=cli.amendp_cli:amendp_cli',
            'aamend=cli.aamend_cli:aamend_cli',
            'aamendp=cli.aamendp_cli:aamendp_cli',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='gitone',
    name='gitone',
    package_dir={"": "src"},
    packages=setuptools.find_packages('src'),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/marskar/gitone',
    version='0.1.3',
    zip_safe=False,
)
