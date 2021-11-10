from setuptools import setup, find_packages

setup(
    name='teste',
    version='1',
    url='https://github.com/gorillascode/quiteja-crediativos-ws-lib-py',
    license='',
    author='GorillasCode Software Design',
    author_email='devops@gorillascode.com',
    description='Biblioteca para integração com o Webservice da CrediAtivos',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests>=2.21.0',
        'zeep==3.4.0',
        'python-dateutil==2.8.1',
        'cachetools>=3.1.1'
    ]
)
