from setuptools import setup

setup(name='easy_etl',
      version='0.1.0',
      description='A framework for ETL development with PySpark',
      url='https://github.com/r4z3c/easy_etl',
      author='Cezar Almeida',
      author_email='cezar.almeidajr@gmail.com',
      license='MIT',
      packages=['easy_etl', 'tools'],
      install_requires=['envparse', 'simple-settings'],
      zip_safe=False)
