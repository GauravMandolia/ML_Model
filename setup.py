from setuptools import find_packages, setup

# Constant
HYP_E_DOT = '-e .'


def get_requirements(file_path: str) -> list:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYP_E_DOT in requirements:
            requirements.remove(HYP_E_DOT)
            
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='GauravMandolia',
    author_email='g.k.mandolia@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)
