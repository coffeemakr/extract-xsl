import os
from setuptools import setup

lib_folder = os.path.dirname(os.path.realpath(__file__))
requirementPath = lib_folder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()


setup(
    name='extract_xsl',
    version='0.1',
    url='https://github.com/coffeemakr/extract_xsl',
    license='MIT',
    author='coffeemakr',
    author_email='extract_xsl@unstable.ch',
    description='Tool to extract tables of Excel files',
    install_requires=install_requires,
    scripts=[
        "scripts/extract-xsl"
    ]
)
