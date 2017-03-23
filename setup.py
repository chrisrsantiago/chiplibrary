import os
import sys

from setuptools import setup, find_packages

try:
    assert sys.version_info >= (3,2)
except AssertionError:
    print('Python >= 3.2.x is required to run chiplibrary.')
    sys.exit(0)

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

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
    'pyjwkest',
    'lxml',
    'libsass',
    'mistune',
    'munch',
    'webhelpers2',
    'whoosh',
    'wtforms',
    'python-social-auth',
    'social-auth-app-pyramid',
    'inflect',
    'romkan'
    ]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov'
    ]

setup(name='chiplibrary',
      version='1.4',
      description='chiplibrary',
      long_description=README,
      classifiers=[
          'Programming Language :: Python',
          'Framework :: Pyramid',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
      ],
      author='Christopher Santiago',
      author_email='admin@chiplibrary.net',
      url='http://github.com/chrisrsantiago/chiplibrary',
      keywords='web wsgi pylons pyramid megaman battle network',
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
      chiplibrary_createschema = chiplibrary.scripts.createschema:main
      chiplibrary_loadchips = chiplibrary.scripts.loadchips:main
      chiplibrary_buildindex = chiplibrary.scripts.buildindex:main
      """,
      )
