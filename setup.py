from setuptools import setup, find_packages

setup(
    name='neuragens-cli',
    version='1.0.0-alpha',
    author='Michael Douglas Barbosa Araujo',
    author_email="michaeldouglas010790@gmail.com",
    description='The NeuraGens CLI is a command-line interface tool that you use to initialize, develop, scaffold, and maintain NeuraGens applications directly from a command shell.',
    packages=find_packages(),
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "neuragen=cli.cli:cli",
        ],
    },
    zip_safe=False,
)