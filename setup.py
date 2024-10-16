from setuptools import setup, find_packages
from pathlib import Path

readme_path = Path(__file__).parent / 'README.md'
with open(readme_path, 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='neuragens-cli',
    version='1.0.1',
    author='Michael Douglas Barbosa Araujo',
    author_email="michaeldouglas010790@gmail.com",
    description='The NeuraGens CLI is a command-line interface tool that you use to initialize, develop, scaffold, and maintain NeuraGens applications directly from a command shell.',
    long_description=long_description,
    long_description_content_type='text/markdown',  # Especifica o tipo do conteúdo
    packages=find_packages(),
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "neuragen=cli.cli:cli",
        ],
    },
    zip_safe=False,
)
