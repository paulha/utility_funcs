from setuptools import setup

install_requires = {
      'os',
      'unittest',
      'yaml'
}

setup(name='utility_funcs',
      version='0.1',
      description='Utilities for useful actions that I keep repeating...',
      url='https://github.com/paulha/utility_funcs.git',
      author='Paul Hanchett',
      author_email='paul.hanchett@gmail.com',
      license='MIT',
      packages=['utility_funcs'],
      zip_safe=False)