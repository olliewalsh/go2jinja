#
# Copyright Contributors to the Eclipse BlueChi project
#
# SPDX-License-Identifier: LGPL-2.1-or-later
from setuptools import find_packages, setup


def readme():
    with open("README.md") as desc:
        return desc.read()


setup(
    name="go2jinja",
    version="0.1.0",
    description="Library for converting Go Templates to Jinja Templates",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Michael Engel",
    url="https://github.com/engelmi/go2jinja",
    license="LGPL-2.1-or-later",
    install_requires=[
        "regex>=2024.11.6",
    ],
    packages=find_packages(),
    include_package_data=True,
    package_data={"go2jinja": ["py.typed"]},
    zip_safe=True,
    keywords=["go2jinja", "python", "Go", "template", "Jinja"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.9",
)
