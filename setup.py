#!/usr/bin/env python

PROJECT = 'rovicli'

# Change docs/sphinx/conf.py too!
VERSION = '0.1'

from setuptools import setup, find_packages

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

setup(
    name=PROJECT,
    version=VERSION,

    description='Command line access to the Rovi API',
    long_description=long_description,

    author='Devin Sevilla',
    author_email='dasevilla@gmail.com',

    url='https://github.com/dasevilla/rovicli',
    download_url='https://github.com/dasevilla/rovicli/tarball/master',

    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    scripts=[],

    provides=[],
    install_requires=['distribute', 'cliff', 'cliff-tablib'],

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'rovicli = rovicli.main:main'
        ],
        'rovicli': [
            'search_amgvideo = rovicli.search:AmgVideoSearch',
            'search_video = rovicli.search:VideoSearch',
            'search_music = rovicli.search:MusicSearch',
            'artwork = rovicli.info:ArtworkInfo',
            'info_video = rovicli.info:VideoInfo',
            'info_episode = rovicli.info:EpisodeInfo',
            'info_season = rovicli.info:SeasonInfo',
        ],
    },

    zip_safe=False,
)
