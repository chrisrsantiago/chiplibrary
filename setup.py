import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'pyramid_dogpile_cache2',
    'pyramid_tm',
    'mako',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'libsass',
    'mistune',
    'scrapy',
    'webhelpers2',
    ]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov'
    ]

setup(name='chiplibrary',
      version='0.0.1',
      description='chiplibrary',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Christopher Santiago',
      author_email='',
      url='http://github.com/chrisrsantiago/chiplibrary',
      keywords='web wsgi bfg pylons pyramid megaman battle network',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = chiplibrary:main
      [console_scripts]
      initialize_chiplibrary_db = chiplibrary.scripts.initializedb:main
      """,
      )
