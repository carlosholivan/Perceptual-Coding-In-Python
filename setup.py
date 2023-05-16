from setuptools import setup

setup(
    name="peaq",
    version="0.0",
    description="A Python package for computing PEAQ (Perceptual Evaluation of Audio Quality) in Python 3",
    author="",
    author_email="",
    packages=["peaq"],
    install_requires=[
        "numpy==1.23.5",
        "librosa==0.10.0"
    ],
)