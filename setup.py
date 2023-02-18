#!/usr/bin/env python


from distutils.core import setup
import pathlib

HERE = pathlib.Path(__file__).parent
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding="utf-8")

setup(
    name="PY-packArch",
    version="1.5.4",
    description="Small library to manage pacman package manager and install AUR",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Tom5521",
    author_email="mismarttv321@gmail.com",
    url="https://github.com/Tom5521/PY-pacman",
    py_modules=["packarch"],
    keywords=["pacman", "arch linux"],
    download_url="https://github.com/Tom5521/PY-pacman/archive/refs/tags/1.5.4.tar.gz",
    license="GPL-3.0",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Unix",
        "Topic :: System :: Software Distribution",
    ],
)
