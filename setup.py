import setuptools

with open("README.md", "r", encoding="utf-8") as fr:
    recipe = fr.read()

setuptools.setup(
    name="example-pkg-scdev-pd-columns",
    version="0.0.1",
    author="HAN HOJIN",
    author_email="seupjak@korea.ac.kr",
    description="Data De-identification Tool in KOR Language",
    long_description=recipe,
    long_description_content_type="text/markdown",
    url="https://github.com/SeupInitial/",
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    package_dir={"": "ko-data-de-identification"},
    package=setuptools.find_packages(where="ko-data-de-identification"),
    python_requires=">=3.11",
)