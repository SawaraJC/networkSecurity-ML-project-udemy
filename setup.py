from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    Docstring for get_requirements
    
    :return: Description
    :rtype: List[str]

    This function will return the list of requirements
    """

    requirement_lst:List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            #read lines
            lines = file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("Requirements file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Sanwara Chandak",
    packages=find_packages(),
    install_requires=get_requirements()
)