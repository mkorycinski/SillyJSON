from setuptools import setup, find_packages

with open('./requirements.txt', 'r') as rfile:
    reqs = [req for req in rfile.read().split('\n') if req]

setup(
    name='SillyJSON',
    version='0.0.1',
    description='A rather silly implementation of JSON '
                'parsing with some help from regular expressions.',
    long_description=f'{open("README.md").read()}',
    author='Mateusz Koryciński',
    author_email='mateusz.korycinski@outlook.com',
    url='https://github.com/mkorycinski/SillyJSON',
    install_requires=reqs,
    packages=find_packages(exclude=['*tests*']),
)
