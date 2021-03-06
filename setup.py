import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="awsm-cli",
    version="0.0.3",
    description="CLI menu for awesome list https://github.com/sindresorhus/awesome",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/rand-net/awsm-cli",
    author="rand-net",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["awsm_cli"],
    include_package_data=True,
    entry_points={"console_scripts": ["awsm-cli = awsm_cli.__init__:main"]},
    install_requires=["art", "prompt-toolkit", "requests"],
    keywords=["awesome list", "awesome", "resources", "lists", "mammoths"],
)
