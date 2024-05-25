from setuptools import setup, find_packages

setup(
    name='latindict',
    version='0.1.0',
    packages=find_packages(),
    author='hikarukbit',
    author_email='hikaru_dano@vk.com',
    description='A simple library for fetching Latin word data from Wiktionary.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hikarukbit/latindict',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
