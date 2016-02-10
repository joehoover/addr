from setuptools import setup

setup(name='addr',
      version='0.1',
      description='Functions for implementing Aggregate Distributed Dictionary Representation',
      #url='',
      author='Joe Hoover',
      author_email='jehoover@usc.edu',
      license='USC',
      packages=['addr'],
      install_requires=[
          'numpy==1.8.0',
          'scipy==0.13.0',
          'scikit-learn==0.17.0',
          'pandas==0.16.0',
          'gensim==0.11.1-1'
      ],
      zip_safe=False)

