from setuptools import setup, find_packages

setup(name='python_console_menu',
      version='1.0',
      url='https://github.com/lukewarlow/python_console_menu',
      author='Luke Warlow',
      author_email='lukewarlow156@gmail.com',
      description='A simple library to handle the menus for your python console applications.',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      classifiers=("Programming Language :: Python :: 3",
                   "License :: OSI Approved :: Apache Software License",
                   "Operating System :: OS Independent"))
