from setuptools import setup

setup(name='FAIRtools',
      version='0.1',
      description='FAIR Metrics Evaluation Tool',
      url='https://github.com/wilkinsonlab/FAIR_Evaluator_Client',
      classifiers=[
        'Programming Language :: Python :: 2.7',
        'Topic :: Evaluation :: FAIR Principles',
      ],
      author='Mario Prieto',
      author_email='mario.prieto@upm.es',
      license='Wilkinson Laboratory',
      packages=['FAIRtools'],
      #install_requires=['urllib', 'simplejson', 'requests'],
      zip_safe=False)