import setuptools

import hello_world

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='hello-world',
    version=hello_world.__version__,
    description='Hello World Python Package',
    url='https://github.com/juwaini/hello-world-py-package',
    author='Juwaini',
    author_email='juwaini@gmail.com',
    license='Juwaini',
    packages=setuptools.find_packages(),
    zip_safe=False,
    install_requires=requirements
)
