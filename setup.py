from setuptools import setup, find_packages

setup(
    name='format_mac',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'format_mac=format_mac.cli:main',
        ],
    },
)
