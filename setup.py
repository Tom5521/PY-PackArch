from setuptools import setup

setup(
    name="PY-packArch",
    version="1.9.3-1",
    author="Tom5521",
    author_email="mismarttv321@gmail.com",
    description="Small library to manage pacman package manager and install packages from AUR",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.10",
    license="GPL-3.0",
    keywords=["pacman", "arch linux", "linux", "AUR"],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Unix",
        "Topic :: System :: Software Distribution",
        "Environment :: Console",
    ],
    url="https://github.com/Tom5521/PY-PackArch",
    project_urls={
        "Bug Tracker": "https://github.com/Tom5521/PY-PackArch/issues",
        "Documentation": "https://github.com/Tom5521/PY-PackArch/blob/master/README.md",
        "Download-url": "https://github.com/Tom5521/PY-PackArch/archive/refs/heads/master.zip",
    },
    install_requires=["Tom-Toolbox"],
)
