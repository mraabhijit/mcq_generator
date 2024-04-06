from setuptools import find_packages, setup

setup(
    name='mcq_generator',
    version='0.0.1',
    author='Abhijit Chakraborty',
    author_email='ab.chakraborty@outlook.com',
    install_requires=['openai', 'langchain', 'streamlit',
                      'python-dotenv', 'PyPDf2'],
    packages=find_packages()
)