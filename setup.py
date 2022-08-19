from setuptools import setup, find_packages

setup(
    name="main", 
    packages=find_packages("src"), 
    package_dir={'': 'src'}
)