import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="devstat",
    version="0.0.1",
    author="Prashant Divate",
    author_email="diwateprashant44@gmail.com",
    description="A system status library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prashantdivate/devstat",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)