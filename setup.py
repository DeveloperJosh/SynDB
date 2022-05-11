from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name="SynDB",
    version="1.7",
    description="simple database using json.",
    long_description_content_type="text/markdown",
    long_description=long_description,
    author="Josh Wells",
    author_email="bam0909@outlook.com",
    license="MIT",
    url="https://github.com/Synterra-Technologies/SynDB",
    py_modules=['syndb'],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Database',
    ],
)