import os

from setuptools import setup

ROOT = os.path.dirname(os.path.realpath(__file__))
with open("README.md", encoding="utf-8") as inp:
    README_CONTENT = inp.read()


setup(
    # Meta data
    name="scrapx",
    # Package files
    package_dir={
        "scrapx": "src/scrapx",
        "tests": "tests",
    },
    packages=["scrapx"],
    include_package_data=True,
    # Dependencies
    install_requires=[
        "weblib>=0.1.28",
        "six",
        "user_agent",
        "selection",
        "lxml",
        "defusedxml",
    ],
    extras_require={
        "full": ["urllib3", "certifi"],
    },
    # Topics
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
    ],
)