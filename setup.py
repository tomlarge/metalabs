from setuptools import setup, find_packages

setup(name='Metalabs',
      version='0.1',
      url='https://github.com/tomlarge/metalabs',
      license='MIT',
      author='Tom LARGE',
      author_email='large.tom.pro@gmail.com',
      description='simplifies the process of managing metalabs keys',
      packages=find_packages(),
      long_description=open('README.md').read(),
      zip_safe=False)
