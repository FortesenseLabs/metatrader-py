import io
from setuptools import setup, find_packages


def readme():
    with io.open("README.md", encoding="utf-8") as f:
        return f.read()


def requirements(filename):
    with io.open(filename, encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]


setup(
    name="metatrader",
    version="0.0.1",
    packages=find_packages(),
    url="",
    download_url="",
    license="GPL-3.0",
    author="Fortesense Labs",
    author_email="fortesenselabs@gmail.com",
    description="Metatrader API Interface Client for Python",
    long_description=readme(),
    long_description_content_type="text/markdown",
    install_requires=requirements(filename="requirements.txt"),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3",
    keywords=", ".join(
        [
            "metatrader",
            "f-api",
            "historical-data",
            "financial-data",
            "stocks",
            "funds",
            "etfs",
            "indices",
            "currency crosses",
            "bonds",
            "commodities",
            "crypto currencies",
            "synthetic instruments",
            "trading",
            "investment",
            "portfolio",
            "backtesting",
            "quantitative analysis",
        ]
    ),
    project_urls={
        "Bug Reports": "https://github.com/FortesenseLabs/metatrader-py/issues",
        "Source": "https://github.com/FortesenseLabs/metatrader-py",
        "Documentation": "",
    },
)
