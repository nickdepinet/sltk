from setuptools import setup

setup(name='sltk',
      version='0.1',
      description="Spoken Language Toolkit",
      url='http://github.com/nickdepinet/sltk',
      author='Nick Depinet',
      author_email='depinetnick@gmail.com',
      license='MIT',
      packages=['sltk'],
      install_requires=['python_speech_features'],
      zip_safe=False)
