from setuptools import setup, find_packages

setup(
  name='turkle-monitoring',
  version='0.1.0',
  packages=find_packages(),
  install_requires = [
    "pandas",
    "numpy",
    "matplotlib",
    "sklearn"
  ],
  author="Turkle",
  author_email="info@turkle.io",
  description="Monitoring package for credit scoring models",
  url="link to public github repo",
  classifiers=[
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.11',
  ]
)