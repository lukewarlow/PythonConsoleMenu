from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name='python_console_menu',
    version='1.1.0',
    author='Luke Warlow',
    author_email='projects@warlow.dev',
    description='A simple library to handle the menus for your python console applications.',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/lukewarlow/python_console_menu',
    packages=find_packages(exclude=['demo']),
    keywords=["console menu", "menu", "console"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"
    ]
)
