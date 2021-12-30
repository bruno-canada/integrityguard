#!/usr/bin/env python3

from appdirs import *
from setuptools import setup, find_packages
from colorama import init, Fore, Back, Style
import os

init(autoreset=True)

# Identify OS config default path
os_dirs = AppDirs("IntegrityGuard", "IntegrityGuard")

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ 'appdirs>=1.4.4','watchdog>=1.0.2', 'colorama>=0.4.4' ]

test_requirements = [ ]

setup(
    author="Bruno Bueno",
    author_email='integrityguard@fastmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Multiplatform agent for file integrity monitoring. Monitors, generate logs, and notify.",
    entry_points={
        'console_scripts': [
            'integrityguard=integrityguard.cli:main',
        ],
    },
    data_files=[
        (os_dirs.user_config_dir, ['src/helpers/integrityguard.conf'])
    ],
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='integrityguard',
    name='integrityguard',
    packages=find_packages(include=['integrityguard', 'integrityguard.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/bruno-canada/integrityguard',
    version='0.1.1',
    zip_safe=False,
)

# Print basic instructions for the user
print(Fore.GREEN + "Success!! See important information below:")
print(Fore.YELLOW + "Default config file path: " + os.path.join(os_dirs.user_config_dir, "integrityguard.conf") )
print(Fore.YELLOW + "Default hashes store path: " + os.path.join(os_dirs.user_data_dir, "hashes.json") )