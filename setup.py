from distutils.core import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(name='pq-tool',
      version='0.1.1',
      description='pickle-query Tool',
      author='Salvador Pardiñas',
      author_email='darkfm@vera.com.uy',
      scripts=['bin/pq'],
      url='https://github.com/kouta-kun/pq',
      long_description=long_description,
      long_description_content_type='text/markdown'
)
