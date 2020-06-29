from setuptools import setup, find_packages
import os, sys

del os.link

setup(
    name='football-cli',
    version='0.1.1.1',
    description='A Football CLI with support for live results.',
    author='Alex Munger',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords="""football soccer league scores standings tables
                fixtures matches data live api tool cli""",
    author_email='munger.alex@gmail.com',
    url='https://github.com/amunger3/soccer-cli',
    packages=find_packages(),
    include_package_data = True,
    install_requires=[
        "click>=5.0",
        "requests>=2.7.0"
    ] + (["colorama>=0.3.3"] if "win" in sys.platform else []),
    entry_points={
        'console_scripts': [
            'soccer = soccer.main:main'
        ],
    }
)
