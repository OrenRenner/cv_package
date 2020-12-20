import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cv_package",
    version="0.0.1",
    author="Nishanov Emil",
    author_email="nero19970610@mail.ru",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OrenRenner/cv_package.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=['>=3.6', 'opencv-python==3.4.2.16', 'opencv-contrib-python==3.4.2.16'],
)
