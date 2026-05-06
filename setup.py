from setuptools import setup

setup(
    name="sort-tracker",
    version="1.0.0",
    py_modules=["sort"],
    install_requires=[
        "numpy",
        "filterpy",
        "scipy",
    ],
)
