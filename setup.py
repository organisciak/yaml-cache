from setuptools import setup, find_packages

setup(
    name='yaml_cache',
    version='0.1.0',
    description='A simple YAML-based cache library for Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Peter Organisciak',
    author_email='organisciak@gmail.com',
    url='https://github.com/organisciak/yaml-cache',
    packages=find_packages(),
    install_requires=[
        'PyYAML>=5.1',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)