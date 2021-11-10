import setuptools

setuptools.setup(
    name='teste',
    version='0.0.1',
    url='https://github.com/jeffersonnunesfonseca/packaging-tutorial',
    author='Jefferson Nunes Fonseca',
    author_email='jeffersonnunesfonseca@gmail.com',
    description='Exemplo de como transformar um módulo em package',
    package_dir={"": "src"}, # diz que pasta raiz é o src
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
