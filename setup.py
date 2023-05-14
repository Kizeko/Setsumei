from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A Python Japanese helper library for retrieving information from the JMdict, Kanjidic2,' \
              ' and parsing Japanese text.'


setup(
    name='setsumei',
    version=VERSION,
    project_urls={
        "Issues": "https://github.com/Kizeko/setsumei/issues",
        "Source": "https://github.com/Kizeko/setsumei"
    },
    keywords=['dictionary', 'japanese', 'kanji', 'tokenizer', 'japanese-language', 'japanese-study',
              'jmdict', 'JMndict', 'kanjidic2', 'KRADFILE', 'japanese-dictionary', 'setsumei'],
    license='MIT',
    author='Kizeko',
    install_requires=['janome'],
    author_email='paul.j.petibon@gmail.com',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['setsumei'],
    package_data={'setsumei': ['data/*.sql', 'data/*.json', 'data/*.gz', 'data/*.xml']},
    include_package_data=True,
    platforms='any',
    # Reference: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=['Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 'Programming Language :: Python :: 3.9',
                 'Natural Language :: Japanese',
                 'Natural Language :: English',
                 'Environment :: Plugins',
                 'Intended Audience :: Developers',
                 'Topic :: Database',
                 'Topic :: Text Processing :: Linguistic',
                 'Topic :: Software Development :: Libraries :: Python Modules']
)