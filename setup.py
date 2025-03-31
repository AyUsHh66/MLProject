from setuptools import setup, find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
     requirements=[]
     with open(file_path) as file_obj:
         requirements=file_obj.readlines()
         requirements=[req.replace("\n","") for req in requirements]
         if '-e .' in requirements:
             requirements.remove('-e .')
     return requirements
     
     

setup(
    name='MLProject',
    version='0.0.1',
    author='Ayush Mishra',
    author_email='am2161@srmist.edu.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)