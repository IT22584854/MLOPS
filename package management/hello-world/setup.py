from setuptools import setup, find_packages

#Setuptools : simplifies the creation, management, and distribution of Python projects.
# setup: define metadata and configurations for the package.
# find_packages:automatically discovers all packages and subpackages project directory.
setup(
    name="hello_world_rash321", #unique name of your package.
    version="0.0.1",
    author="Nachiketh",
    author_email="nachiketh@manifoldailearning.in",
    url="https://www.manifoldailearning.in", #A homepage URL for the package or project.
    description="A hello-world example package",
    packages=find_packages(), #Automatically search and includes all Python modules and submodules within the project directory.
    classifiers=[ #compatibility and requirements.
        "Programming Language :: Python :: 3", #Indicates that the package is compatible with Python 3
        "License :: OSI Approved :: MIT License",#package uses the MIT license.
        "Operating System :: OS Independent", #Indicates that pacage should work across various ecosystem of operating system.
    ],
)
