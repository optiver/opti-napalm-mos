"""setup.py file."""
from setuptools import setup, find_packages

__author__ = "Benny Holmgren <benny@holmgren.id.au>"

with open("requirements.txt", "r") as fs:
    reqs = [r for r in fs.read().splitlines() if (len(r) > 0 and not r.startswith("#"))]

setup(
    name="opti-napalm-mos",
    version="4.0.2",
    packages=find_packages(),
    author="Benny Holmgren, Brandon Ewing, ",
    author_email="benny@holmgren.id.au, brandon.ewing@warningg.com, ams_pypi@optiver.com",
    description="Optiver's fork of NAPALM-MOS",
    classifiers=[
        "Topic :: Utilities",
        "Programming Language :: Python",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    url="https://github.com/napalm-automation-community/napalm-mos",
    include_package_data=True,
    install_requires=reqs,
    python_requires=">=3.7",
)
