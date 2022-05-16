import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wts",
    version="1.0.0",
    author=" Lux Luth",
    author_email="luxusluth@gmail.com",
    description="wts is a small packages for write sql statements in a sqlite database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Chaton-mechant/WTS",
    project_urls={
        "Bug Tracker": "https://github.com/Chaton-mechant/WTS/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
