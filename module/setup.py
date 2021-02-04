import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-obis-van-kenobis",
    version="0.0.1",
    author="Ovidijus",
    author_email="ovidijus@example.com",
    description="A small example package of Calculator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ovidijusku/calc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
