import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Aruodas_web_scrapper",
    version="0.0.1",
    author="Ovidijus",
    author_email="ovidijus@example.com",
    description="A small example package of web scrapper that extracts apartments data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ovidijusku/vilnius_apartments/tree/main/module",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
