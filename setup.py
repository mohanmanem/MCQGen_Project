from setuptools import find_packages, setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Mohan Sai',
    author_email='manemmohan.217@gmail.com',
    install_requires=["openai", "langchain", "streamlit", "python-dotenv", "PyPDF2","pandas","numpy"],
    packages=list(find_packages())  # Pass the result of find_packages() as a list
)