import setuptools

with open("README.md", "r", encoding="utf-8") as fr:
    recipe = fr.read()

setuptools.setup(
    name="example-pkg-scdev-pd-columns",
    version="0.1.0",
    author="HAN HOJIN",
    author_email="seupjak@korea.ac.kr",
    description="All-In-One Data De-identification Tool in Korean",
    long_description=recipe,
    long_description_content_type="text/markdown",
    url="https://github.com/SeupInitial/",
    keywords=[
        "데이터",
        "비식별화",
        "가명처리",
        "가명화",
        "암호화",
        "교환 방법",
        "총계처리",
        "부분총계",
        "라운딩",
        "재배열",
        "삭제",
        "식별자 삭제",
        "식별자 부분삭제",
        "레코드 삭제",
        "식별요소 전부삭제",
        "범주화",
        "감추기",
        "랜덤 라운딩",
        "범위방법",
        "제어 라운딩",
        "마스킹",
        "임의 잡음 추가",
        "공백과 대체",
        "Data",
        "Pseudonymization",
        "Aggregation",
        "Reduction",
        "Suppression",
        "Masking"
    ],
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
