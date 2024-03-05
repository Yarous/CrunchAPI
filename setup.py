from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='CrunchAPI',
  version='0.0.1',
  author='Yarous',
  author_email='topecode2001@gmail.com',
  description='This is a API module for CodeCrunch WEBSite!',
  long_description=readme(),
  long_description_content_type='Nothing here',
  url='Github.com/Yarous',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: WINDOWS/LINUX/MACOS/OSX'
  ],
  keywords='files speedfiles ',
  project_urls={
    'GitHub': 'github.com/Yarous'
  },
  python_requires='>=3.6'
)