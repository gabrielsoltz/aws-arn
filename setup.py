from setuptools import setup

setup(
    name="aws-arn",
    version="0.0.18",
    description="A library to work with AWS ARNs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=["aws_arn"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "aws-arn = aws_arn:main",
        ],
    },
    author="Gabriel Alejandro Soltz",
    author_email="gabriel@3ops.com",
    project_urls={
        "Source code": "https://github.com/gabrielsoltz/aws-arn",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


# python3 setup.py sdist bdist_wheel
# twine upload dist/*
