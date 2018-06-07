import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyHTTPD",
    version="0.0.1",
    author="汪心禾",
    author_email="wang__xin_he@163.com",
    description="A simple HTTP server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Wangxinhe2006/PyHTTPD",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
