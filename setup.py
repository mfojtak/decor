import codecs
from setuptools import setup, find_packages

with codecs.open('README.md', 'r', 'utf8') as reader:
    long_description = reader.read()


with codecs.open('requirements.txt', 'r', 'utf8') as reader:
    install_requires = list(map(lambda x: x.strip(), reader.readlines()))


setup(
    name='deco',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/mfojtak/deco',
    license='MIT',
    author='mfojtak',
    author_email='mfojtak@seznam.cz',
    description='deco',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=install_requires,
    scripts=['export_to_serving.py', 'server.py'],
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
