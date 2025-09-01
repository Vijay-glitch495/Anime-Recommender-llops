from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ANIME-RECOMMENDER",
    version="0.1",
    author="Vijay Kumar Reddy Bommireddy",
    packages=find_packages(),
    install_requires = requirements,
)


#python -m pip install -e .