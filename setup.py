import setuptools

setuptools.setup(
    name='teste',
    version='1',
    url='https://github.com/jeffersonnunesfonseca/packaging-tutorial.git',
    author='Jefferson Nunes Fonseca',
    author_email='jeffersonnunesfonseca@gmail.com',
    description='Exemplo de como transformar um módulo em package',
    packages=setuptools.find_packages(where="src")
)
