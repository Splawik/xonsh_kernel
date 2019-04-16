from setuptools import find_packages, setup

setup(name='xonsh_kernel',
      version=' '0.4.1',
      requires=['metakernel',],
      packages=find_packages(include=['xonsh_kernel', 'xonsh_kernel.*']),
      classifiers=[
          'Framework :: IPython',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 2',
          'Topic :: System :: Shells',
      ]
)
