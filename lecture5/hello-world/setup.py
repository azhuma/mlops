from setuptools import setup, find_packages

setup(
    name="hello_world_my_package",
    version="0.0.1",
    author="akylbekz",
    author_email="akylbekz@gmail.com",
    url="https://www.google.com",
    description="A hello-world example package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)