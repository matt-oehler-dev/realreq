import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="realreq",
    version="0.1.0",
    author="Tyler Calder",
    author_email="calder-ty@protonmail.com",
    description="CLI tool to gather dependencies for imports actually used by your code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    python_packages=["_realreq"],
    python_requires=">=3.5",
)

