import pathlib

from setuptools import setup, find_packages


HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()


setup(
    name="tobacco",
    version="1.0.4",
    description="Function pipelines for python",
    author="Robert Enzmann",
    url="https://github.com/renzmann/tobacco",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    license="MIT",
)
