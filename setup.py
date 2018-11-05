from setuptools import setup

setup(
    name='pyromine',
    version='1.0.0',
    description='minecraft server sorftware written in python',
    author='Clark Dwain Luna @chaineater',
    author_email='chain_eater@outlook.com',

    entry_points = {
        'console_scripts': [
            'pyromine = pyromine.__main__:main'
        ]
    }
)