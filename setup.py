import pyromine
from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

requirements = []

setup(
    name='pyromine',
    version=pyromine.__version__,
    description='a mcpe python server',
    long_description=readme,
    author='Clark Dwain Luna',
    author_email='lclarkdwain@outlook.com',
    url='https://github.com/pyromine/pyromine',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': [
            'pyromine = pyromine.__main__:main'
        ]
    },
    install_requires=requirements
)