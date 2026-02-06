from setuptools import setup, find_packages

setup(
    name="easygradients",
    version="0.1.0",
    author="DraxonV1",
    description="A library to easily apply gradients and colors to terminal text.",
    long_description=open('README.md').read() if open('README.md') else "",
    long_description_content_type="text/markdown",
    url="https://github.com/DraxonV1/easygradients",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
