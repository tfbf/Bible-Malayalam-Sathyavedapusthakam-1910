from setuptools import setup, find_packages

setup(name='svpm',
      version='0.1.0',
      description='Scripts to manage digital Sathyavedapusthakam content',
      packages=find_packages(),
      zip_safe=False,
      author='Baiju Muthukadan',
      install_requires=['setuptools',
                        'requests',
                        'Jinja2',
                        'Parsley', # Requires Python 3 patch:
                                   # https://github.com/python-parsley/parsley/pull/18
                        ],
      entry_points={
          'console_scripts': [
              'svpm=svpm.main:run',
          ],
      },
      )
