from pathlib import Path
from setuptools import setup, find_packages

this_dir = Path(__file__).parent.resolve()
readme_path = this_dir / 'README.md'
with readme_path.open('r', encoding='utf-8') as f:
    long_description = f.read()

setup(name='rconfig',
      version='1.1',
      packages=find_packages(),
      description='Python config',
      install_requires=['addict', 'pyyaml'],
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='rivergold',
      author_email='jinghe.rivergold@gmail.com',
      license='MIT')
