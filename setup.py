from setuptools import setup


setup(name='LassoBench',
      packages=['LassoBench'],
      install_requires=[
          'sparse-ho @ https://github.com/QB3/sparse-ho/archive/master.zip',
          'celer @ git+https://github.com/mathurinm/celer.git@eef3bb5',
          'pyDOE',
          'libsvmdata',
          'ax-platform',
          'matplotlib>=2.0.0',
          'numpy>=1.12',
          'scipy>=0.18.0',
          'scikit-learn>=0.21',
          'seaborn>=0.7',
          'pyDOE>=0.3.8'],
      )
