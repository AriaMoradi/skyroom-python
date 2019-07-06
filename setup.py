from setuptools import setup
import sys

requires = ['requests>=2.22.0']
if sys.version_info < (2, 6):
    requires.append('simplejson')

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="skyroom",
    py_modules=['skyroom'],
    version="1.0.0",
    description="Skyroom Python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Aria Moradi",
    author_email="aria.moradi007@gmail.com",
    url="https://github.com/AriaMoradi/skyroom-python",
    keywords=["skyroom", "api"],
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Conferencing",
    ]
)
